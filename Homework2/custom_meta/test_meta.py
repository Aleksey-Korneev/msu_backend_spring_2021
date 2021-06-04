"""This module contains tests for custom metaclass."""

import unittest
from custom_meta import CustomMeta


class TestClass(metaclass=CustomMeta):
    """
    Test class for testing custom metaclass.
    """

    attribute = 0

    def __init__(self):
        self.item = 1
        pass

    def __str__(self):
        return 'qwerty'

    def method(self):
        pass


class TestName(unittest.TestCase):
    """
    Check the names of the metaclass attributes, methods, and magic methods.
    """

    def test_attr_name(self):
        self.assertTrue(hasattr(TestClass, "custom_attribute"))
        self.assertFalse(hasattr(TestClass, "attribute"))

    def test_method_name(self):
        self.assertTrue(hasattr(TestClass, "custom_method"))
        self.assertFalse(hasattr(TestClass, "method"))

    def test_magic_method_name(self):
        self.assertFalse(hasattr(TestClass, "custom___init__"))
        self.assertTrue(hasattr(TestClass, "__init__"))
        tmp = TestClass()
        self.assertEqual(str(tmp), 'qwerty')


    def test_class_name(self):
        self.assertEqual(TestClass.__name__, "custom_TestClass")
        self.assertNotEqual(TestClass.__name__, "TestClass")

    def test_created_in_init(self):

        self.assertTrue(hasattr(TestClass(), "custom_item"))
        self.assertFalse(hasattr(TestClass(), "item"))


if __name__ == "__main__":
    unittest.main()
    tmp = TestClass()
