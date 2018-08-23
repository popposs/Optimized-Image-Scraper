from flask import Flask, request, make_response, Response, jsonify, render_template
from flask_cors import CORS
from multiprocessing import Process, Value
import time

from src.logic.reddit import get_top_posts, cache_posts
from src.logic.channels import CHANNELS
import os


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/urls', methods=['GET'])
def get_post():
    return jsonify({'urls': get_top_posts()})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def update_cache(loop_on):
    while True:
        if loop_on.value == True:
            for channel in CHANNELS:
                cache_posts(channel)
                time.sleep(1)

if __name__ == '__main__':
    p = Process(target=update_cache, args=(Value('b', True),))
    p.start()
    app.run(debug=True, use_reloader=False, host='0.0.0.0')
    p.join()


