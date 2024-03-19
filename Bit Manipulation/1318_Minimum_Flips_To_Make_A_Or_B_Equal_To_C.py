def minFlips(self, a:int, b:int, c:int) ->  int:
    """
    This function calculates the minimum number of bit flips required to convert 'a' to 'c' or 'b' to 'c'.
    
    Each bit in the binary representation of 'a', 'b', and 'c' is considered separately.
    For each bit, if the bit in 'a' and 'b' are not equal to the bit in 'c', then at least one bit flip is required.
    If both 'a' and 'b' have 1s in that bit position, then both bits need to be flipped to match 'c'.
    Otherwise, only one bit flip is needed.

    :param a: The first integer in the range [0, 2^30)
    :param b: The second integer in the range [0, 2^30)
    :param c: The target integer in the range [0, 2^30)
    :return: The minimum number of bit flips required to convert 'a' to 'c' or 'b' to 'c'
    
    
    Time Complexity : O(n), where n is the number of bits in the input integers
    Space Complexity : O(1)
    
    """
    for i in range(30):
        x,y,z = a >> i & 1, b  >> i & 1, c >> i & 1
        if x | y !=z:
            ans = ans + 2 if x == 1 and y == 1 else 1
    return ans