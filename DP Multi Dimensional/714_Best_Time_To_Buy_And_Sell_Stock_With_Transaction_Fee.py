class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        f0, f1 = -float('inf'), 0
        
        for x in prices:
            
            a0, a1 = f0, f1
            f1 = max(a1, a0 + x)
            f0 = max(a0, a1 - x - fee)
        return f1