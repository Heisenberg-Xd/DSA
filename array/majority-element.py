# finding the element that appears more than ⌊n/2⌋ times

def Majoritywins(arr):
    n = len(arr)
    arr.sort()
    candidate=arr[n//2]
    count=0

    for num in arr:
        if num == candidate:
            count+=1

    if count>n//2:
        return candidate
    else:
        return -1
    
if __name__ == "__main__":
    arr=[20,21,21,21,21,22,23]

print(Majoritywins(arr))