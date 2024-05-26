#!/usr/bin/env python3
"""
Unit tests for utils.py module.
"""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[int, Dict]) -> None:
        """
        Tests that access_nested_map returns the correct value
        for the given path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple[str]) -> None:
        """
        Tests that access_nested_map raises a KeyError for invalid paths.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Unit tests for get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self,
                      test_url: str,
                      test_payload: Dict[str, bool]) -> None:
        """
        Tests that get_json returns the correct JSON payload from the URL.
        """
        config = {'return_value.json.return_value': test_payload}
        with patch('requests.get',
                   autospec=True,
                   **config) as mock_request_get:
            self.assertEqual(get_json(test_url), test_payload)
            mock_request_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Unit tests for memoize decorator.
    """

    def test_memoize(self) -> None:
        """
        Tests that memoize caches the result of the method.
        """

        class TestClass:
            """
            A class with a memoized method for testing.
            """
            def a_method(self):
                """
                A simple method that returns 42.
                """
                return 42

            @memoize
            def a_property(self):
                """
                A memoized property that returns the result of a_method.
                """
                return self.a_method()

        with patch.object(TestClass,
                          'a_method',
                          return_value=42) as mock_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
