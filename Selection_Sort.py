def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1 , len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i] , arr[min_index] = arr[min_index], arr[i]

arr = [3,5,63,1,43,688,4]
selectionSort(arr)
print("Sorted array: ")
for i in range(len(arr)):
   print("%d" %arr[i], end = " ")