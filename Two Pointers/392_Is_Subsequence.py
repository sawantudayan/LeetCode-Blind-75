def isSubsequence(self, s:str, t:str) -> bool:
    """This function checks if the string 's' is a subsequence of the string 't'. 
    A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. 
    The function uses two pointers, 'i' and 'j', to iterate through the strings 's' and 't'. 
    If the 'i'th character of 's' matches the 'j'th character of 't', the pointer 'i' is incremented. Otherwise, the pointer 'j' is incremented. 
    The function returns True if all characters in 's' are matched, and False otherwise. 
    
    
    Time complexity = O(m+n), where 'm+n' is the length of the strings 't'.
    Space  complexity = O(1).
    """
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j] :
            i +=1
        j +=1
    return i==len(s)