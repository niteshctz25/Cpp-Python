def linear_search(arr,item,start = 0):
    for i in range(start , len(arr)):
        if arr[i] == item:
            return i
    return -1

arr = [12,3,5,6,7,8,4,9,15,17,18,65]
item = int(input("Enter the number you want to search: "))
result = linear_search(arr,item)
if result == -1:
    print("Element not found")
else:
    print("Element found at position: " + str(result))