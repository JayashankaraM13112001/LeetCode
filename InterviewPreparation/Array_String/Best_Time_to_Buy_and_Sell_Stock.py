'''
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

def maxProfit(self, prices: list[int]) -> int:
        maxp=0
        left=0
        right=1
        while right<len(prices):
            if prices[left]<prices[right]:
                profit=prices[right]-prices[left]
                maxp=max(maxp,profit)
            else:
                left=right
            right+=1

        return maxp