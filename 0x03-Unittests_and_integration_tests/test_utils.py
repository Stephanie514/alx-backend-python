#!/usr/bin/env python3
"""
This tests for utils.py module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


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

        Args:
            nested_map (dict): The nested dictionary.
            path (tuple): The path to access the nested value.
            expected_result: The expected result when accessing
            the nested value.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
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
