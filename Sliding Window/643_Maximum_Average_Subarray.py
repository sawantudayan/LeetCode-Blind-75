def findMaxAverage(self, nums: List[int], k: int) -> float:
    """
    The function findMaxAverage takes in two arguments, nums which is a list of integers and k which is an integer representing the size of the subarray.

    The function first initializes a variable s with the sum of the first k elements of the list nums.

    Then it initializes a variable ans with the value of the variable s.

    Next, it uses a for loop to iterate over the list nums starting from the k-th element, 
    and for each iteration, it updates the variable s by adding the current element of the list and subtracting the (i-k)th element of the list.

    The function also uses a variable ans to keep track of the maximum average of a subarray of size k.

    Finally, it returns the variable ans/k which contains the maximum average of a subarray of size k in the list nums.
    
    Time Complexity : O(n), where n is the length of the list
    Space Complexity : O(1).
    """
    s = sum(nums[:k])
    ans = s
    for i in range(k, len(nums)):
        s += nums[i] - nums[i-k]
        ans = max(ans, s)
    return ans/k