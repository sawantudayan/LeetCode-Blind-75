def maxOperations(self, nums: List[int], k:int) -> int:
   """
   This function finds the maximum number of pairs in a list of integers that can be formed such that the sum of any pair is equal to a given positive integer 'k'.

   The list of integers and 'k' are given as input to the function. 
   The list is first sorted in ascending order. 
   Then, starting from the first and last indices of the sorted list, the function checks if the sum of the numbers at these indices equals 'k'. 
   If it does, the indices are incremented and decremented respectively, and the count of pairs is incremented. 
   If the sum is greater than 'k', the index of the larger number is decremented, and if the sum is less than 'k', the index of the smaller number is incremented. 
   This process continues until the indices cross each other. The final count of pairs is then returned as output.

   Time Complexity  : O(nlogn), where n is the length of the input list
   Space Complexity : 0(1), since only variables used in the function are 'l'and 'r'
   """
   nums.sort()
   l, r, ans = 0, len(nums)-1, 0
   while l < r:
       s = nums[l] + nums[r]
       if s == k:
           ans += 1
           l +=1
           r -= 1
       elif s > k:
           r -=1
       else:
           l +=1
   return ans