def binary_search(array,item):
    lowerBound = 0;
    upperBound = len(array) - 1
    midPoint = 0
    while (lowerBound <= upperBound):
        midPoint = (lowerBound + upperBound) // 2
        if array[midPoint] < item:
            lowerBound = midPoint + 1
        elif array[midPoint] > item:
            upperBound = midPoint - 1
        else:
            return midPoint
    return -1

array = [1,2,3,4,5,6,7,8,9]
item = int(input("Enter the number you want to search: "))
result = binary_search(array,item)
if result != 1:
    print("Element is found at index " + str(result)) 
else:
    print("Element not found")

