def longestOnes(self, nums: List[int], k: int) -> int:
    """
    Initialize l (left pointer) and r (right pointer) to -1. This indicates that the function hasn't started processing the array yet.
    
    Enter a while loop that continues as long as the right pointer is less than the length of the array minus 1.
    
    Increment the right pointer by 1 (move it to the right).
    
    Check if the current element is 0. If so, subtract 1 from the k value, which keeps track of the remaining zeros allowed.
    
    If k is now negative, it means there are too many consecutive zeros in the current subarray. In this case, increment the left pointer by 1 to remove the leftmost zero from the subarray. If the leftmost element is also a zero, add 1 back to k since it was a zero that we're allowed to have.
    
    Return the difference between the right and left pointers, which is the length of the longest subarray that meets the criteria of having at most k zeros.
    
    Time Complexity : O(n), where n is the length of the string
    Space  Complexity : O(1), where l,r, k utilizes the constant space.
    """
    l = r = -1
    while r < len(nums) - 1:
        r += 1
        if nums[r] == 0:
            k -= 1
        if k < 0:
            l += 1
            if nums[l] == 0:
                k += 1
    return r - l