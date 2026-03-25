#finding the second largest number in array

def Getsecondlargest(arr):

    n =len(arr)
    arr.sort()

    return arr[n-2]

if __name__ == "__main__":
    arr=[2,7,1,6,9,5]

    print(Getsecondlargest(arr))