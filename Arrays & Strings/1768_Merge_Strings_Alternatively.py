def mergeAlternatively(self, word1: str, word2: str) -> str:
    """
    This method concatenates two input strings `word1` and `word2` by alternating the characters
    from each string, starting with `word1`. If the strings have different lengths, the method
    pads the shorter string with an empty string until it matches the length of the longer string.

    :param word1: The first input string
    :param word2: The second input string
    :return: A new string that is the concatenation of `word1` and `word2` interleaved
    
    Time complexity: O(m+n), where m, n are the lengths of the string
    Space complexity: O(m)
    """
    return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
