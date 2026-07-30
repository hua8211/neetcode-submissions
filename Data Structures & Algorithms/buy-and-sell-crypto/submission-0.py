class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        max = 0 
        while r <= len(prices)-1:
            buy = prices[l]
            sell = prices[r]
            print(buy, sell)
            curr = sell - buy
            if curr > max:
                # l = r
                # r += 1
                max = curr
            if sell < buy:
                l = r
                r += 1
            else:
                r += 1
        return max