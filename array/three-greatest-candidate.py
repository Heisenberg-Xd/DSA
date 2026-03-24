#finding a maximum product of a largest 3 digits in the array 

def greatestCandidate(arr):
    n=len(arr)

    arr.sort()

    option1 = arr[n-1]*arr[n-2]*arr[n-3]
    option2 = arr[0]*arr[1]*arr[n-1]

    return max(option1,option2)
if __name__ == "__main__":
    arr = [-10, -3, 5, 6, -20]

    print(greatestCandidate(arr))
 
   