#Stock Buy and Sell (Max one transaction)

def MaxProfit(prices):
    n=len(prices)
    res=0

    for i in range(n-1):
        for j in range(i+1,n):
            res = max(res,prices[j]- prices[i])

    return res 

if __name__ == "__main__":
    price=[230,430,120,100,800,760]

    print(MaxProfit(price))