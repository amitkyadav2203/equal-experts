from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """
    Provide instructions for using the API when the root URL is accessed.
    """
    return jsonify({
        'message': 'Please provide a GitHub username in the path, e.g., /octocat, to retrieve public Gists for that user.'
    }), 400


@app.route('/<username>', methods=['GET'])
def get_gists(username):
    """
    Fetch and return the publicly available Gists for a given GitHub username.
    """
    url = f"https://api.github.com/users/{username}/gists"
    response = requests.get(url)
    
    if response.status_code == 200:
        gists = response.json()
        gist_list = [{'id': gist['id'], 'url': gist['html_url'], 'description': gist['description']} for gist in gists]
        return jsonify(gist_list), 200
    else:
        return jsonify({'error': 'User not found or GitHub API request failed'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)

