from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/fetch', methods=['GET'])
def fetch_website():
    pass


if __name__ == '__main__':
    app.run(debug=True)
