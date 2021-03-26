class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0
        
        minprice = sys.maxsize
        maxprofit = 0
        
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            if prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        
        return maxprofit