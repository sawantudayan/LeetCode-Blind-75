def pivotIndex(self, nums: List[int]) -> int:
    """
    Finds the pivot index of a list of integers.

    The pivot index is the index of a number in the list such that the sum of the numbers on its left is equal to the sum of the numbers on its right.

    Args:
        nums (List[int]): A list of integers.

    Time  Complexity: O(n)
    Space Complexity: O(1)
    """
    left, right = 0, sum(nums)
    for i, x in enumerate(nums):
        right = right - x
        if left == right:
            return i
        left = left + x