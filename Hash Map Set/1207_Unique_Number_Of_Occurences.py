from collections import Counter

def function(arr):
   """
   This function checks if all elements in the input list have distinct frequencies.

   :param arr: list, required. A list of integers.
   :return: bool. True if all elements have distinct frequencies, False otherwise.

   Time complexity: O(n), where n is the length of the input list, iterating through the list once to fill the counter, 
   and another time to check the distinct values.

   Space complexity: O(n), where n is the length of the input list. The additional space is used to store the counter.
   """
   cnt = Counter(arr)
   return len(set(cnt.values())) == len(cnt)