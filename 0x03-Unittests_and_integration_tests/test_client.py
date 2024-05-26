#!/usr/bin/env python3
"""
Tests for client.py module
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Defines integration tests for GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method to mock requests.get.
        """
        cls.get_patcher = patch('requests.get', side_effect=cls.get_payload)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to stop the patcher.
        """
        cls.get_patcher.stop()

    @classmethod
    def get_payload(cls, url):
        """
        Mock payloads for different URLs.
        """
        if url == "https://api.github.com/orgs/google":
            return Mock(status_code=200, json=lambda: cls.org_payload)
        if url == "https://api.github.com/orgs/google/repos":
            return Mock(status_code=200, json=lambda: cls.repos_payload)
        return Mock(status_code=404)

    def test_public_repos(self):
        """
        Test public_repos method.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos method with license argument.
        """
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


class TestGithubOrgClient(unittest.TestCase):
    """
    Defines unit tests for GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test org method.
        """
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.return_value = {}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {})
        mock_get_json.assert_called_once_with(expected_url)

    def test_public_repos_url(self):
        """
        Test _public_repos_url method.
        """
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {"repos_url": "http://testurl.com/repos"}
            client = GithubOrgClient("test_org")
            self.assertEqual(
                client._public_repos_url,
                "http://testurl.com/repos"
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test public_repos method.
        """
        expected_repos = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = expected_repos
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = "http://testurl.com/repos"
            client = GithubOrgClient("test_org")
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("http://testurl.com/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test has_license method.
        """
        client = GithubOrgClient("test_org")
        self.assertEqual(
            client.has_license(repo, license_key),
            expected_result
        )


if __name__ == "__main__":
    unittest.main()
