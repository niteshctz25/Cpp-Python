def insertionSort(arr):
    for i in range(len(arr)):
        value = arr[i]                        
        hole = i - 1
        while (hole >= 0 and value < arr[hole]):
            arr[hole + 1 ] = arr[hole]
            hole = hole - 1
        arr[hole + 1] = value

arr = [12,11,13,5,6]
insertionSort(arr)
print("sorted array: ")
for i in range(len(arr)):
    print("%d" %arr[i])


"""
        value = arr[i]
        hole = i
        while hole >0 and value < arr[hole-1] :
            arr[hole] = arr[hole - 1]
            hole -= 1
        arr[hole] = value

 """
