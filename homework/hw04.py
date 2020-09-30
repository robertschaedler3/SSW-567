import requests
import sys
import functools

GITHUB_API = 'https://api.github.com'


def get_repos_json(owner):
    res = requests.get(f'{GITHUB_API}/users/{owner}/repos')
    return [repo['name'] for repo in res.json()]


def get_commits(owner, repo):
    res = requests.get(f'{GITHUB_API}/repos/{owner}/{repo}/stats/contributors')
    return sum([contrib['total'] for contrib in res.json()])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python hw04.py <Github username>')
        sys.exit(1)

    owner = sys.argv[1]

    data = [(repo, get_commits(owner, repo)) for repo in get_repos_json(owner)]

    # print results
    for repo, commit_count in data:
        print(f'{repo}: {commit_count}')
