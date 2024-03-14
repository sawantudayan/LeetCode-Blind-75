class RecentCounter:
   """
   A class to maintain a list of time stamps of the last 3000ms and provide a method to ping with a time stamp and return the number of pings in the last 3000ms.
   """

   def __init__(self):
       """
       Initialize a RecentCounter object with an empty list to store time stamps.
       """
       self.s = []  # Time complexity: O(1)

   def ping(self, t: int) -> int:
       """
       Add the given time stamp t to the list and return the number of pings in the last 3000ms.

       :param t: int, the time stamp to add
       :return: int, the number of pings in the last 3000ms

       Time complexity:
       Adding an element to the list takes O(1) time.
       Finding the index of the smallest timestamp greater than t-3000 takes O(log n) time using the bisect_left function.
       Therefore, the overall time complexity is O(log n).

       Space complexity:
       The space complexity is O(n) where n is the number of time stamps stored in the list.
       """
       self.s.append(t)  # Time complexity: O(1)
       return len(self.s) - bisect_left(self.s, t-3000)  # Time complexity: O(log n)