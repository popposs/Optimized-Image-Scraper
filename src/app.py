from flask import Flask, request, make_response, Response, jsonify
from flask_cors import CORS
from reddit import get_top_posts

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_post():
    return jsonify({'channels': get_top_posts()})

if __name__ == '__main__':
    app.run(debug=True)
