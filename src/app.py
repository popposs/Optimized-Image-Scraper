from flask import Flask, request, make_response, Response, jsonify, render_template
from flask_cors import CORS
from multiprocessing import Process, Value
import time

from src.logic.reddit import get_top_posts, cache_posts
from src.logic.channels import CHANNELS
from src.logic.cache import cache_client

from src.utils.downloads import download_images, setup_download_dir
from src.utils.db_utils import db_checks

import os


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/urls/', defaults={'page': 0})
@app.route('/urls/<int:page>', methods=['GET'])
def get_post(page):
    urls = cache_client.get('urls_{}'.format(page))
    if urls is None:
        return jsonify({ 'urls': get_top_posts() })
    else:
        urls = [ url.replace('\'', '').strip() for url in urls[1:-1].split(',') ]
        return jsonify({ 'urls' : urls })

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def update_cache(loop_on):
    while True:
        if loop_on.value == True:
            for index, channel in enumerate(CHANNELS):
                urls = cache_posts(channel)
                print('Channel:', channel)
                download_images(download_dir, urls)
                cache_client.set('urls_{}'.format(index), urls)
                time.sleep(1)

if __name__ == '__main__':
    db_checks()
    download_dir = setup_download_dir()
    p = Process(target=update_cache, args=(Value('b', True),))
    p.start()
    app.run(debug=True, use_reloader=False, host='0.0.0.0')
    p.join()


