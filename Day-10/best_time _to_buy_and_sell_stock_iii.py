class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        if l<=1:
            return 0
        buys=[[0]*3 for _ in range(l+1) ]
        sells=[[0]*3 for _ in range(l+1)]
        buys[1][1] = -prices[0]
        buys[1][2] = -math.inf
        for i in range(2,l+1):
            for j in range(1,3):
                buys[i][j]=max(buys[i-1][j],sells[i-1][j-1] - prices[i-1])
                sells[i][j]=max(sells[i - 1][j], buys[i - 1][j] + prices[i - 1])
        return max(sells[l][0], max(sells[l][1], sells[l][2]))
