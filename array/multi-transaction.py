#Stock Buy and Sell ...Multi transaction

def MaxMultiProfit(prices):
    res=0
    
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            res += prices[i]-prices[i-1]

    return res



if __name__ == "__main__":
    price=[230,430,120,100,800]


print(MaxMultiProfit(price))