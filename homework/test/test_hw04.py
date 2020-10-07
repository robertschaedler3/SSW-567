import unittest
from unittest.mock import patch

import hw04

OWNER = 'robertschaedler3'
REPO = 'SSW-567'
COMMITS = 100


class TestHw4(unittest.TestCase):

    @patch('hw04.get_repos')
    def test_get_repos(self, mock_get_repos):
        mock_get_repos.return_value = [REPO]

        repos = hw04.get_repos(OWNER)
        self.assertIsInstance(repos, list)
        for item in repos:
            self.assertIsInstance(item, str)

    @patch('hw04.get_commits')
    def test_get_commits(self, mock_get_commits):
        mock_get_commits.return_value = COMMITS

        commits = hw04.get_commits(OWNER, REPO)
        self.assertIsInstance(commits, int)
