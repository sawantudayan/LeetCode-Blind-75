def productExceptSelf(self, nums: List[int]) -> List[int]:
    """
    Calculates the product of all elements in the input list, excluding the current element, for each position.

    This function takes a list of integers `nums` as an input and returns a new list of integers as output.
    The output list contains the product of all elements in the input list "around" each element, 
    i.e., the product of all elements to the left and right of the current element, excluding the current element itself.

    Parameters:
    nums (list[int]): The input list of integers.

    Returns:
    list[int]: A new list of integers, where the i-th element is the product of all elements in the input list, excluding the current element at the i-th position.
    
    Time Complexity =  O(n), where n is the length of the array
    Space Complexity = O(1)

    """
    n = len(nums)
    ans = [0] * n
    left = 1
    right = 1
    for i, x in enumerate(nums):
        ans[i] = left
        left = left * nums[i]
    for i in range(n-1, -1, -1):
        ans[i] = ans[i]*right
        right = right * nums[i]
    return ans
