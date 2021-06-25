def quickSort(arr,low,high):
    if low < high :
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
def partition(arr,low,high):
    start = low
    pivot = arr[high]
    for j in range(low,high):
        if (arr[j] <= pivot):
            start = start + 1
            arr[start-1] , arr[j] = arr[j] , arr[start-1]
        arr[start],arr[high] = arr[high],arr[start]
    return (start)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i],end = " ")

        
        
"""
def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

def partition(array, start, end):
    pivot = array[start]
    low = start
    high = end

    while low < high:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]


    array[start], array[high] = array[high], array[start]
    return high

array = [10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)
print(array)

"""