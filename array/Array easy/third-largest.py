#find third largest number in array

def getthirdlargest(arr):
    n = len(arr)

    arr.sort()
    return arr[n-3]

if __name__ == "__main__":
    arr=[12,34,23,56,72,11]

    print (getthirdlargest(arr))