"""Custom list is defined in this module."""

from itertools import zip_longest


class CustomList(list):
    """
    Custom list supporting addition, subtraction and comparison.
    """
    def __add__(self, other):
        return CustomList(lhs + rhs for (lhs, rhs) in
                          zip_longest(self, other, fillvalue=0))

    __radd__ = __add__

    def __sub__(self, other):
        return CustomList(lhs - rhs for (lhs, rhs) in
                          zip_longest(self, other, fillvalue=0))

    def __rsub__(self, other):
        return -self + other

    def __neg__(self):
        return CustomList(-item for item in self)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)
