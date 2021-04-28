from itertools import zip_longest

class CustomList(list):
    """
    Custom list supporting addition, subtraction and comparison.
    """
    def __add__(self, other):
        return CustomList(map(lambda item : item[0] + item[1], \
            zip_longest(self, other, fillvalue = 0)))

    def __sub__(self, other):
        return CustomList(map(lambda item : item[0] - item[1], \
            zip_longest(self, other, fillvalue = 0)))

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)
