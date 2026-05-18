import httpx
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = "Satya-roy"  # change to any GitHub username

def fetch_repos(username):
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=5"
    
    with httpx.Client() as client:
        response = client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

def summarise(username):
    repos = fetch_repos(username)
    print(f"\n GitHub Summary for @{username}")
    print("=" * 40)
    for repo in repos:
        print(f"\n  {repo['name']}")
        print(f"   Stars    : {repo['stargazers_count']}")
        print(f"   Language : {repo['language'] or 'N/A'}")
        print(f"   Desc     : {repo['description'] or 'No description'}")

if __name__ == "__main__":
    summarise(USERNAME)