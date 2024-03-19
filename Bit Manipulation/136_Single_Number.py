def singleNumber(self, nums: List[int]) -> int:
    """
    This function takes a list of integers as input and returns the integer that appears only once in the list.
    The function uses the XOR bitwise operation to find the unique number.
    The XOR operation has the following properties:
    - it is commutative (a ^ b ^ c = a ^ c ^ b)
    - it is distributive (a ^ (b ^ c) = (a ^ b) ^ c)
    - any number XORed with zero gives the number itself (a ^ 0 = a)

    The function initializes a result variable to zero and iterates over the input list.
    For each number in the list, it performs a XOR operation with the current result.
    Since XOR operation has the property that if we XOR a number with itself, it will give zero,
    all the duplicate numbers in the list will cancel out and the final result will be the unique number.
    
    Time Complexity : O(n), where n is the length of the input
    Space Complexity : O(1), which means it uses a constant amout of memory regardless of the size of the input list. 
    """
    res = 0
    for num in nums:
        res = res ^ num
    return res