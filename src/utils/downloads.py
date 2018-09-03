# Adapted from https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python
import json
import os
import logging
from queue import Queue
from pathlib import Path
from urllib.request import urlopen, Request
from threading import Thread
from time import time

from models.base import db
from models.url_model import URLS
from sqlalchemy import exists

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            directory, link = self.queue.get()
            try:
                download_path = download_link(directory, link)
                insert_url(directory, link)
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
        if get_url(url) is None:
            print('Queueing {}'.format(url), flush=True)
            queue.put((directory, url))

    queue.join()
    logging.info('Took %s', time() - ts)

def get_url(url):
    return db.query(URLS.url).filter_by(url=url).first()

def insert_url(download_path, url):

    url_ = get_url(url)

    if url_:
        return

    new_url = URLS(url=url, host_path=str(download_path))

    db.begin_nested()
    try:
        db.add(new_url)
        db.commit()
    except IntegrityError as e:
        db.rollback()
    except:
        db.rollback()