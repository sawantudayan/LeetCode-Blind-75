from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
   """
   This function checks if two given strings are close strings or not.
   Two strings are said to be close if they contain the same letters in their integer counts, up to rearrangement, and have the same length.
   
   Time Complexity: O(n log n) due to the sorting operation
   Space Complexity: O(n) as we are storing the counts of characters in the string.
   """
   cnt1 = Counter(word1)
   cnt2 = Counter(word2)
   return sorted(cnt1.values()) == sorted(cnt2.values()) and set(cnt1.keys()) == set(cnt2.keys())