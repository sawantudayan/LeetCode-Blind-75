def reverseVowels(self, s: str) -> str:
    """
    Reverses the order of the vowels in the given string `s`.

    This function first converts the input string `s` to a list `s`. It then creates an empty list `res` and appends the indices
    of the characters in `s` to `res`. The function then iterates over half of the length of `res`, swapping the characters
    at the indices `res[i]` and `res[-i-1]` in `s`. Finally, the function joins the characters in `s` back into a string
    and returns the result.

    Args:
        s (str): The input string containing vowels to reverse.

    Returns:
        str: The input string `s` with the vowels reversed.
        
        
    Time Complexity = O(n)
    Space Complexity = O(n)

    """
    res = []
    s = list(s)
    for i in range(len(s)):
        if (s[i] in "aeiouAEIOU"):
                res.append(i)
    for i in range(len(res)//2):
            s[res[i]], s[res[-i-1]] = s[res[-i-1]],s[res[i]]
    return "".join(s)
