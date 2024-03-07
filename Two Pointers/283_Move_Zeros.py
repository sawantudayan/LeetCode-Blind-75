def moveZeros(self, nums: List[int]) -> None:
   """
   This function takes a list of integers as input and moves all zeros to the end of the list while maintaining the relative order of the non-zero elements. 
   It uses the 'in-place' method, which means that the original list is modified directly without creating a new list. 
   The function uses two pointers, 'i' and 'j', to iterate through the list. 
   If an element is non-zero, it swaps the element with the element at the 'i'th index and increments 'i'. 

    Time complexity - O(n), where 'n' is the length of the input list. 
    Space complexity - O(1)

   """
   i = -1
   for j, x in enumerate(nums):
       if x:
           i += 1
           nums[i], nums[j] = nums[j], nums[i]
