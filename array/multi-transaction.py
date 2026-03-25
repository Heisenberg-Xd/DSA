#Stock Buy and Sell (Max one transaction)

def MaxMultiProfit(prices):
    res=0
    
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            res += prices[i]-prices[i-1]

    return res

if __name__ == "__main__":
    price=[230,430,120,100,800,760]

print(MaxMultiProfit(price))