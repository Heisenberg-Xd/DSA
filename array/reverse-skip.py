#reverse an array in a group of k then skip next group and then again reverse

def reverseArrayInGroup(arr,k):
    i=0
    n=len(arr)

    while i<n:
        left=i
        right=min(i+k-1,n-1)

        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        i+=2*k



if __name__ == "__main__":
    arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    k=4

    reverseArrayInGroup(arr,k)
    print(" ".join(map(str,arr)))