def findMaxAverage(self, nums: List[int], k: int) -> float:
    """
    This function returns the maximum average of a subarray of size 'k'.

    Parameters:
    nums (List[int]): A list of integers in the subarray.
    k (int): The size of the subarray.

    Returns:
    float: The maximum average of a subarray of size 'k'.
    
    Time Complexity : O(n), where n is the length of the list
    Space Complexity : O(1).
    """
    s = sum(nums[:k])
    ans = s
    for i in range(k, len(nums)):
        s += nums[i] - nums[i-k]
        ans = max(ans, s)
    return ans/k