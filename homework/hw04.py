import requests
import sys
import functools

GITHUB_API = 'https://api.github.com'


def get_repos(owner):
    repos = []
    try:
        res = requests.get(f'{GITHUB_API}/users/{owner}/repos')
        repos = [repo['name'] for repo in res.json()]
    except Exception as e:
        pass
    return repos


def get_commits(owner, repo):
    commits = 0
    try:
        res = requests.get(f'{GITHUB_API}/repos/{owner}/{repo}/stats/contributors')
        commits = sum([contrib['total'] for contrib in res.json()])
    except Exception as e:
        pass
    return commits


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python hw04.py <Github username>')
        sys.exit(1)

    owner = sys.argv[1]

    data = [(repo, get_commits(owner, repo)) for repo in get_repos(owner)]

    # print results
    for repo, commit_count in data:
        print(f'{repo}: {commit_count}')
