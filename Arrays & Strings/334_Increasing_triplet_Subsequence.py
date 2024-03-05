def increasingTriplet(self, nums: List[int]) -> bool:
   """
   Determines if there exists a triplet in the given list of integers where the first element is less than the second element and the second element is less than the third element.

   This function uses a two-pointer approach to iterate through the list of integers. 
   It initializes two variables `mi` and `mid` to infinity. 
   For each number in the list, if the number is greater than `mid`, it returns True as this implies the existence of an increasing triplet. 
   If the number is less than or equal to `mi`, it updates `mi` to the current number. Otherwise, it updates `mid` to the current number. 
   If the function iterates through the entire list without finding an increasing triplet, it returns False.

   :param nums: List[int] - A list of integers
   :return: bool - True if an increasing triplet is found, False otherwise
   
   Time Complexity = O(n), where n is the lenght of the input list
   Space Complexity = O(1), uses the constant amount of memory to store variable mi, mid, num
   """
   mi, mid = float('inf'), float('inf')
   for num in nums:
       if num > mid:
           return True
       if num <= mi:
           mi = num
       else:
           mid = num
   return False
