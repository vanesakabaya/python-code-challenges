# function declaration 
def Swaps(arr, n):
     
    swaps = 0
    temp = arr.copy()
    m = {}
 
    temp.sort()
 
    for i in range(n):
        m[arr[i]] = i
    init = 0
    #swapping loop to check in array loop
    for i in range(n):
        if (arr[i] != temp[i]):
            swaps += 1
            init = arr[i]
            arr[i], arr[m[temp[i]]] = arr[m[temp[i]]], arr[i]
            m[init] = m[temp[i]]
            m[temp[i]] = i
             
    return swaps

#entering the elements in array
num = []

n = int(input("Enter array length: "))
for ItemsArray in range(1, n + 1):
    item = int(input("Enter item %d in array: " %ItemsArray))
    num.append(item)
#check the lenght of array
length = len(num)
print("Array: ", num)
print("Minimum number of swapps required to sort an array is: ", Swaps(num, length))