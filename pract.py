def quickSort(arr,low,high):
    if low < high :
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
        
def partition(arr,low,high):
    start = low
    end = high
    pivot = arr[high]
    while(start < end):
        while(arr[start] <= pivot):
          start += 1
        while(arr[end] > pivot):
          end -= 1
        if (start < end):
          arr[start],arr[end] = arr[end],arr[start]
    arr[low],arr[end] = arr[end],arr[low]
        

arr = [ 10, 7, 8, 9, 1, 5 ]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i],end = " ")

        
        
