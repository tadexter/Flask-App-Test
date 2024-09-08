from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/fetch', methods=['GET'])
def fetch_website():
    # Get the URL from the query parameters
    url = request.args.get('url')

    if not url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        # Make a GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Return the content of the website
        return response.text, 200
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
