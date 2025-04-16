import requests
from config import GITHUB_TOKEN

def fetch_repos_by_language(language):
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    query = f"language:{language}+good-first-issues:>0"
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"
    response = requests.get(url, headers=headers)
    return response.json()
