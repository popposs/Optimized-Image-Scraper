# Adapted from https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python
import json
import os
import logging
from queue import Queue
from pathlib import Path
from urllib.request import urlopen, Request
from threading import Thread
from time import time

from models.base import Session
from models.url_model import URLS
from sqlalchemy import exists

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

queue_flush = dict()

class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.db = Session()

    def get_url(self, url):
        return self.db.query(URLS.url).filter_by(url=url).first()

    def run(self):
        while True:
            directory, link = self.queue.get()
            try:
                if self.get_url(link) is None:
                    download_path = download_link(directory, link)
                    new_url = URLS(url=link, host_path=str(download_path))
                    queue_flush[link] = new_url
            finally:
                self.queue.task_done()

def download_link(directory, link):
    download_path = directory / os.path.basename(link)
    with urlopen(link) as image, download_path.open('wb') as f:
        f.write(image.read())
    logger.info('Downloaded %s', link)
    return download_path

def setup_download_dir():
    download_dir = Path('images')
    if not download_dir.exists():
        download_dir.mkdir()
    return download_dir

def download_images(directory, urls):
    ts = time()
    queue = Queue()

    for x in range(4):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()

    for url in urls:
        print('Queueing {}'.format(url), flush=True)
        queue.put((directory, url))

    queue.join()

    db = Session()
    db.add_all(list(queue_flush.values()))
    queue_flush.clear()

    logging.info('Took %s', time() - ts)

