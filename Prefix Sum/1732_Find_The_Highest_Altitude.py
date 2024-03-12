def largestAltitude(self, gain: List[int]) -> int:
   """
   This function returns the maximum altitude that can be reached after applying a list of altitude gains.
   The function works by starting from an initial altitude of 0, then iterating through the list of gains, adding each gain to the current altitude, and updating the maximum altitude if the new altitude is higher.


   Parameters:
   gain (List[int]): A list of integers representing the altitude gains at each step. A positive gain represents going up, while a negative gain represents going down.

   Returns:
   int: The maximum altitude that can be reached after applying the altitude gains in the given list.

   Time Complexity : O(n), where n is the length of the string
   Space Complexity : O(1), uses the constant amount of space to store the current altitude.
   """
   ans = h = 0
   for v in gain:
       h = h + v
       ans = max(ans, h)
   return ans