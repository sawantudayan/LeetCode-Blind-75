def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    """
    Finds the difference between two lists of integers.

    Given two lists of integers `nums1` and `nums2`, 
    returns a list of two lists, where the first list contains the elements of `nums1` that are not present in `nums2`, and the second list contains the elements of `nums2` that are not present in `nums1`.

    Args:
        nums1 (List[int]): The first list of integers.
        nums2 (List[int]): The second list of integers.

    Returns:
        List[List[int]]: A list of two lists, where the first list contains the elements of `nums1` that are not present in `nums2`, and the second list contains the elements of `nums2` that are not present in `nums1`.

    Time Complexity: O(n+m), where n is the length of `nums1` and m is the length of `nums2`. This is because the function performs a single pass over both lists to convert them into sets, and the size of the lists is the dominant term in the time complexity.

    Space Complexity: O(n+m), which is due to the storage of the two sets `s1` and `s2`, as well as the intermediate results computed during the execution of the function.
    """
    s1 = set(nums1)
    s2 = set(nums2)
    return [list(s1 - s2), list(s2 - s1)]