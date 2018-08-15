from flask import Flask, request, make_response, Response, jsonify, render_template
from flask_cors import CORS
from src.logic.reddit import get_top_posts

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/urls', methods=['GET'])
def get_post():
    return jsonify({'channels': get_top_posts()})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
