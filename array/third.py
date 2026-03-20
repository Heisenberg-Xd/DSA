#get missing positive number from array 

def getmissingpositive(arr):
    s = set(arr)

    i=1
    while   True:
        if i not in s:
            return i
        i+=1

if __name__ == "__main__":
        arr=[-1,4,1,2]   

print(getmissingpositive(arr))