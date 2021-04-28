"""This module contains tests for custom metaclass."""

import unittest
from custom_meta import CustomMeta


class TestClass(metaclass=CustomMeta):
    """
    Test class for testingcustom metaclass.
    """

    attribute = 0

    def method(self):
        pass


class TestName(unittest.TestCase):
    """
    Check the names of the metaclass attributes, methods, and magic methods.
    """

    def test_attr_name(self):
        self.assertTrue(hasattr(TestClass, 'custom_attribute'))
        self.assertFalse(hasattr(TestClass, 'attribute'))

    def test_method_name(self):
        self.assertTrue(hasattr(TestClass, 'custom_method'))
        self.assertFalse(hasattr(TestClass, 'method'))

    def test_magic_method_name(self):
        self.assertFalse(hasattr(TestClass, 'custom___new__'))
        self.assertTrue(hasattr(TestClass, '__new__'))


if __name__ == '__main__':
    unittest.main()
