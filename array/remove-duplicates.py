#  Remove duplicates from Sorted Array

def removeDuplicate(arr):
    n=len(arr)
    seen=set()
    idx=0

    for i in range(n):
        if arr[i] not in seen:
            seen.add(arr[i])
            arr[idx] = arr[i]
            idx +=1

    return idx

if __name__ == "__main__":
    arr=[21,21,22,22,22,23,24,25,25,25,25,25,26,27,28,28]

    NewArray=removeDuplicate(arr)

    for i in range(NewArray):
        print(arr[i],end="  ")