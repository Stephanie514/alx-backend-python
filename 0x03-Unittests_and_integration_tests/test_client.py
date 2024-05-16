#!/usr/bin/env python3
"""
Tests for client.py module
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


@parameterized_class([
    {"url": "https://api.github.com/orgs/google", "repos": ["repo1", "repo2"]},
    {"url": "https://api.github.com/orgs/abc", "repos": ["repo3", "repo4"]}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Defines integration tests for GithubOrgClient class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method to mock requests.get
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to stop the patcher
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method
        """
        self.mock_get.return_value.json.return_value = self.repos
        client = GithubOrgClient(self.url)
        self.assertEqual(client.org, self.repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos method with license argument
        """
        self.mock_get.return_value.json.return_value = TEST_PAYLOAD
        client = GithubOrgClient(self.url)
        repos_with_license = client.public_repos('apache-2.0')
        self.assertEqual(repos_with_license, ["repo1", "repo2"])


class TestGithubOrgClient(unittest.TestCase):
    """
    Defines unit tests for GithubOrgClient class
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test org method
        """
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.return_value = {}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {})
        mock_get_json.assert_called_once_with(expected_url)

    @patch('client.GithubOrgClient._public_repos_url', new_callable=Mock)
    def test_public_repos_url(self, mock_public_repos_url):
        """
        Test _public_repos_url method
        """
        org_name = "test_org"
        expected_url = f"https://api.github.com/orgs/{org_name}/repos"
        client = GithubOrgClient(org_name)
        self.assertEqual(client._public_repos_url, expected_url)

    @patch('client.get_json', new_callable=Mock)
    def test_public_repos(self, mock_get_json):
        """
        Test public_repos method
        """
        org_name = "test_org"
        expected_repos = ["repo1", "repo2"]
        mock_get_json.return_value = expected_repos
        client = GithubOrgClient(org_name)
        self.assertEqual(client.public_repos(), expected_repos)
        mock_get_json.assert_called_once_with(client._public_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test has_license method
        """
        client = GithubOrgClient("test_org")
        self.assertEqual(client.has_license(repo, license_key), expected_result)


if __name__ == "__main__":
    unittest.main()
