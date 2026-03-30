#

def twosums(arr,target):
    n=len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == target:
                return True
        
    return False

if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9]
    target=18

if twosums(arr,target):
    print ("True")
else:
    print ("false")
        