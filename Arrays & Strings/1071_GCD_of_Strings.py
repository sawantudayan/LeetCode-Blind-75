def gcdOfStrings(self, str1: str, str2: str) -> str:
   """
   This method returns the greatest common divisor (GCD) of the lengths of two input strings,
   if the concatenation of the two strings is equal to the reversed concatenation.
   If the condition is not met, an empty string is returned.

   :param str1: The first input string
   :param str2: The second input string
   :return: A string representing the GCD of the lengths of the two input strings
   
   Space Complexity -  O(1), because the amount of the memory used does not depend on the size of the input string
   Time Complexity - O(n), where n, is the maximum length of the input string
   """
   if str1 + str2 != str2 + str1:
       return ''
   x = gcd(len(str1), len(str2))
   return str1[:x]

