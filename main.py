from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def fetch_website():
    return "Welcome"


if __name__ == '__main__':
    app.run(debug=True)
