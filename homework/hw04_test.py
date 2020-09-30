import unittest

from hw04 import get_repos, get_commits

# A known valid account name and repository
OWNER = 'robertschaedler3'
REPO = 'SSW-567'


class TestHw4(unittest.TestCase):

    def test_get_repos(self):
        repos = get_repos(OWNER)
        self.assertIsInstance(repos, list)
        for item in repos:
            self.assertIsInstance(item, str)

    def test_get_commits(self):
        commits = get_commits(OWNER, REPO)
        self.assertIsInstance(commits, int)
