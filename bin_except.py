Author: Justin Huang
# GitHub username: huangjus
# Date: 4/25/23
# Description: The code defines a custom exception, TargetNotFound, and a modified binary search function, `bin_except`.
# The function takes a sorted list and a target value as input. It searches for the target using binary search,
# returning its index if found. If the target is not found, the function raises the TargetNotFound exception instead of
# returning -1.

class TargetNotFound(Exception):
    """An exception class to indicate that the target value is not in the list."""
    def __init__(self, message="Target value not found in the list"):
        self.message = message
        super().__init__(self.message)


def bin_except(a_list, target):
    """
    Searches a_list for an occurrence of target
    If found, returns the index of its position in the list
    If not found, raises a TargetNotFound exception
    """
    first = 0
    last = len(a_list) - 1
    while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
            return middle
        if a_list[middle] > target:
            last = middle - 1
        else:
            first = middle + 1
    raise TargetNotFound()
