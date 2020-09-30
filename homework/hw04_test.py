import unittest

from hw04 import get_repos, get_commits

# A known valid account name and repository
OWNER = 'robertschaedler3'
REPO = 'SSW-567'


class TestHw4(unittest.TestCase):

    def test_get_repos(self):
        repos = get_repos(OWNER)
        self.assertIsInstance(list, repos)
        for item in repos:
            self.assertIsInstance(str, get_repos)

    def test_get_commits(self):
        commits = get_commits(OWNER, REPO)
        self.assertIsInstance(int, commits)
