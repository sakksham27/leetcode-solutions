# data structure: Array 
# time complexity: O(n)
# space complexity: O(1)

# Example 
prices = [7,1,5,3,6,4]
print(prices)


def buyAndSell(prices):
    # defined variables
    buy, sell = 0,1
    maxProfit = 0
    while sell < len(prices):
        if prices[buy] < prices[sell]: # you made profit 
            profit = prices[sell] - prices[buy]
            maxProfit = max(profit, maxProfit)   # to check if this profit is the maxProfit 
        else: 
            buy = sell 
        sell = sell + 1
    return maxProfit


print(buyAndSell(prices))
    
