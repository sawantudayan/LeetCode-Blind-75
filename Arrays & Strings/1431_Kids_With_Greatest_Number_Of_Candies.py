def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
   """
   Determines whether each kid can have enough candies to have the most candies of all kids.

   Parameters:
   - candies (list[int]): List of candies for each kid.
   - extraCandies (int): Extra candies that can be given to a kid.

   Returns:
   list[bool]: List of booleans indicating whether each kid can have enough candies.
   
   Time Complexity - O(n), where n is the number of the elements in the candies list, such that the fucntion iterates through the list once to find the maximum
                    number of candies and again to check if each kid has enough candies after adding extra candies.
   Space Complexity - O(n), where n is the number of elements in candies list, such that the maximum number of candies is also stored in a variable, but it only takes
                    up a constant amount of space, so it doesn't affect the overall space complexity.
   """
   maxCandies = max(candies)
   return [candy + extraCandies >= maxCandies for candy in candies]
