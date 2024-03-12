def longestSubarray(self, nums:list[int]) -> int:
   """
   This function returns the length of the longest subarray with equal number of 0's and 1's in a given array of 0's and 1's.
   
   :param nums: A list of integers where each integer is either 0 or 1.
   :return: The length of the longest subarray with equal number of 0's and 1's. If no such subarray exists, it returns 0.
   
   
   Time Complexity : O(n), where n is the length of the strings
   Space Complexity: O(1)
   
   """
   n = len(nums)
   left = [0]*n
   right = [0]*n
   for i in range(1, n):
       if nums[i-1] == 1:
           left[i] = left[i-1]+1
   for i in range (n-2, -1, -1):
       if nums[i+1] == 1:
           right[i] = right[i+1]+1
   return max(a+b for a, b in zip(left, right))