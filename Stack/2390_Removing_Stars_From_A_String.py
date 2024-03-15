def removeStars(self, s: str) -> str:
    """
    It initializes an empty list called ans.
    
    It then iterates through each character c in the input string s.
    
    If the current character c is an asterisk (*), the method removes the last character appended to the ans list by calling ans.pop().
    
    If the current character c is not an asterisk, it appends the character to the ans list by calling ans.append(c).
    
    Finally, it joins all the characters in the ans list into a single string and returns the result.
        
    Time Complexity : O(n), where n is the length of the string 's', as it iterates through each character in the input sting exactly once, and performs a constant number of operations for each character.
    
    Space Complexity : O(n), where n is the length of the input string, as it crated a new list 'ans' to store the modified string, which can grow up to a length of n characters.
    
    """
    ans = []
    for c in s:
        if c == '*':
            ans.pop()
        else:
            ans.append(c)
    return ''.join(ans)