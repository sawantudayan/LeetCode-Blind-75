def decodeString(self, s: str) -> str:
    """
    This function decodes a string that has been encoded using a specific format. 
    
    The input string s should contain digits, letters, and square brackets []. 
    
    The function decodes the string and returns the decoded string.
    
    Time Complexity : O(n), where n is the length of the given string, each character in the string is processed exactly once in the for loop
    Space Complexity : O(n), where n is the length of the string, as the function uses three lists, 's1','s2',and 'res' to store intermediate results.
    
    
    """
    s1, s2 = [], []
    num, res = 0, ''
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '[':
            s1.append(num)
            s2.append(res)
            num, res = 0, ''
        elif c == ']':
            res = s2.pop() + res * s1.pop()
        else:
            res += c
    return res