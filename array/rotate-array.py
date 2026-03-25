#rotate an array by d position ;)
def rotateArray(arr,d):
    n=len(arr)

    for i in range(d):

        first=arr[0]
        for j in range (n-1):
            arr[j]=arr[j+1]

        arr[n-1]=first

if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7,8,9]
    d=2

    rotateArray(arr,d)
    for i in range(len(arr)):
        print(arr[i], end="  ")

