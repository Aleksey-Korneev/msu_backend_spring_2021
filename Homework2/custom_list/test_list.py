"""This module contains tests for custom list."""

import unittest
from custom_list import CustomList
from copy import deepcopy


class TestType(unittest.TestCase):
    """
    Test types of objects obtained by using defined operations.
    """

    def setUp(self):
        self.cl1 = CustomList([0, 1])
        self.cl2 = CustomList(range(3))
        self.l1 = [10, 11, 12, 13]
        self.l2 = list(range(10, 15))

    def test_type(self):
        self.assertTrue(isinstance(self.cl1, CustomList))
        self.assertTrue(isinstance(self.cl1, list))

    def test_type_add(self):
        self.assertTrue(isinstance(self.cl1 + self.cl2, CustomList))
        self.assertTrue(isinstance(self.cl1 + self.l2, CustomList))
        self.assertTrue(isinstance(self.l1 + self.cl2, CustomList))

    def test_type_sub(self):
        self.assertTrue(isinstance(self.cl1 - self.cl2, CustomList))
        self.assertTrue(isinstance(self.cl1 - self.l2, CustomList))
        self.assertTrue(isinstance(self.l1 - self.cl2, CustomList))

    def test_type_neg(self):
        self.assertTrue(isinstance(-self.cl1, CustomList))


class TestAdd(unittest.TestCase):
    """
    Test objects obtained by adding lists and custom lists.
    """

    def setUp(self):
        self.cl1 = CustomList([0, 1])
        self.cl2 = CustomList(range(3))
        self.l1 = [10, 11, 12, 13]
        self.l2 = list(range(10, 15))

    def test_add_CustomList(self):
        self.assertEqual(self.cl1 + self.cl2, CustomList([0, 2, 2]))
        self.assertEqual(self.cl2 + self.cl1, CustomList([0, 2, 2]))
        self.assertEqual(self.cl1 + CustomList(), self.cl1)
        self.assertEqual(self.cl1 + -self.cl1, CustomList([0, 0]))

    def test_add_list(self):
        self.assertEqual(self.cl1 + self.l1, CustomList([10, 12, 12, 13]))
        self.assertEqual(self.cl1 + list(), self.cl1)
        self.assertEqual(
            self.cl1 + list(-item for item in self.cl1), CustomList([0, 0])
        )

    def test_radd_list(self):
        self.assertEqual(self.l1 + self.cl1, CustomList([10, 12, 12, 13]))
        self.assertEqual(list() + self.cl1, self.cl1)
        self.assertEqual(
            list(-item for item in self.cl1) + self.cl1, CustomList([0, 0])
        )


class TestSub(unittest.TestCase):
    """
    Test objects obtained by subtracting lists and custom lists.
    """

    def setUp(self):
        self.cl1 = CustomList([0, 1])
        self.cl2 = CustomList(range(3))
        self.l1 = [10, 11, 12, 13]
        self.l2 = list(range(10, 15))

    def test_sub_CustomList(self):
        self.assertEqual(self.cl1 - self.cl2, CustomList([0, 0, -2]))
        self.assertEqual(self.cl2 - self.cl1, CustomList([0, 0, 2]))
        self.assertEqual(self.cl1 - CustomList(), self.cl1)
        self.assertEqual(self.cl1 - -self.cl1, CustomList([0, 2]))

    def test_sub_list(self):
        self.assertEqual(self.cl1 - self.l1, CustomList([-10, -10, -12, -13]))
        self.assertEqual(self.cl1 - list(), self.cl1)
        self.assertEqual(
            self.cl1 - list(-item for item in self.cl1), CustomList([0, 2])
        )

    def test_rsub_list(self):
        self.assertEqual(self.l1 - self.cl1, CustomList([10, 10, 12, 13]))
        self.assertEqual(list() - self.cl1, -self.cl1)
        self.assertEqual(
            list(-item for item in self.cl1) - self.cl1, CustomList([0, -2])
        )


class TestCmp(unittest.TestCase):
    """
    Test results of comparison between lists and custom lists.
    """

    def setUp(self):
        self.l1 = [0, 1, 2, 3, 4]
        self.l2 = [0, 1, 2, 3, 3]
        self.l3 = [0, 1, 2, 3]
        self.l4 = [0, 1, 2, 3, 4, 5]
        self.cl1 = CustomList(self.l1)
        self.cl2 = CustomList(self.l2)
        self.cl3 = CustomList(self.l3)
        self.cl4 = CustomList(self.l4)

    def test_eq(self):
        self.assertTrue(self.cl1 == self.cl1)
        self.assertTrue(self.cl1 == self.l1)
        self.assertTrue(self.l1 == self.cl1)
        self.assertFalse(
            CustomList([1, 2, 3, 5, 4]) > CustomList([1, 2, 3, 4, 5])
        )

    def test_ne(self):
        self.assertTrue(self.cl1 != self.cl2)
        self.assertTrue(self.cl1 != self.cl3)
        self.assertTrue(self.cl1 != self.cl4)
        self.assertTrue(self.cl1 != self.l2)
        self.assertTrue(self.l3 != self.cl1)

    def test_lt(self):
        self.assertTrue(self.cl2 < self.cl1)
        self.assertTrue(self.cl2 < self.l1)
        self.assertTrue(self.l2 < self.cl1)

    def test_le(self):
        self.assertTrue(self.cl1 <= self.cl1)
        self.assertTrue(self.cl1 <= self.l1)
        self.assertTrue(self.l1 <= self.cl1)
        self.assertTrue(self.cl2 <= self.cl1)
        self.assertTrue(self.cl2 <= self.l1)
        self.assertTrue(self.l2 <= self.cl1)


class TestImmutability(unittest.TestCase):
    """
    Test immutability of custom lists after being used.
    """

    def setUp(self):
        self.l1 = [0, 1, 2, 3, 4]
        self.cl1 = CustomList(self.l1)
        self.cl1_copy = deepcopy(self.cl1)

    def compare_content(self, lhs, rhs):
        self.assertEqual(len(lhs), len(rhs))
        for (lhs_item, rhs_item) in zip(lhs, rhs):
            self.assertEqual(lhs_item, rhs_item)

    def test_immutability_add(self):
        cl_len = len(self.cl1)
        self.cl1 + self.cl1
        self.assertEqual(cl_len, len(self.cl1))
        self.compare_content(self.cl1, self.cl1_copy)
        self.cl1 + self.l1
        self.assertEqual(cl_len, len(self.cl1))
        self.compare_content(self.cl1, self.cl1_copy)
        self.l1 + self.cl1
        self.assertEqual(cl_len, len(self.cl1))
        self.compare_content(self.cl1, self.cl1_copy)

    def test_immutability_sub(self):
        cl_len = len(self.cl1)
        self.assertEqual(cl_len, len(self.cl1))
        self.compare_content(self.cl1, self.cl1_copy)
        self.cl1 - self.cl1
        self.assertEqual(cl_len, len(self.cl1))
        self.compare_content(self.cl1, self.cl1_copy)
        self.cl1 - self.l1
        self.assertEqual(cl_len, len(self.cl1))
        self.compare_content(self.cl1, self.cl1_copy)
        self.l1 - self.cl1
        self.assertEqual(cl_len, len(self.cl1))
        self.compare_content(self.cl1, self.cl1_copy)

    def test_immutability_cmp(self):
        cl_len = len(self.cl1)
        self.cl1 < self.cl1
        self.assertEqual(cl_len, len(self.cl1))
        self.compare_content(self.cl1, self.cl1_copy)
        self.cl1 < self.l1
        self.assertEqual(cl_len, len(self.cl1))
        self.compare_content(self.cl1, self.cl1_copy)
        self.l1 < self.cl1
        self.assertEqual(cl_len, len(self.cl1))
        self.compare_content(self.cl1, self.cl1_copy)
        self.cl1 == self.cl1
        self.assertEqual(cl_len, len(self.cl1))
        self.compare_content(self.cl1, self.cl1_copy)
        self.cl1 != self.cl1
        self.assertEqual(cl_len, len(self.cl1))
        self.compare_content(self.cl1, self.cl1_copy)

    def test_immutability_neg(self):
        cl_len = len(self.cl1)
        -self.cl1
        self.assertEqual(cl_len, len(self.cl1))
        self.compare_content(self.cl1, self.cl1_copy)


if __name__ == "__main__":
    unittest.main()
