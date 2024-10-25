import json
import requests


def get_languages(repo_name):
    user, repo = repo_name.split('/')
    print(f"user: {user}, repo: {repo}")
    url = f"https://api.github.com/repos/{user}/{repo}/languages"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise ConnectionError
    except ConnectionError as err:
        print(f"Error {err} while making/getting response from {url}")
        return False 