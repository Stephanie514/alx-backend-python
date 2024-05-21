#!/usr/bin/env python3
"""
This tests for utils.py module
"""
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit test class for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        This test access_nested_map function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in nested map")
    ])
    def test_access_nested_map_exception(
        self, nested_map, path, expected_exception_message
    ):
        """
        Test access_nested_map function with exceptions.
        """
        # Asserting that a KeyError is raised with the expected message
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_exception_message)


class TestGetJson(unittest.TestCase):
    """
    Test class for the get_json function.
    """

    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json function.
        """
        # Configuring the mock to return a mock response
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Calling the function to test
        result = get_json(test_url)

        # Assertions
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test class for the memoize decorator.
    """

    def test_memoize(self):
        """
        Test memoize decorator.
        """

        # Defining a test class
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Patching the a_method of the TestClass
        with patch.object(TestClass, 'a_method') as mock_method:
            # Creating an instance of TestClass
            test_instance = TestClass()

            # Calling the memoized property twice
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

            # Asserting that the method was called only once
            mock_method.assert_called_once()

            # Asserting that the results are equal
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
