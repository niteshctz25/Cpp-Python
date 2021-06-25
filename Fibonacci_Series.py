n = int(input("Enter the numbers of terms: "))
n1 = 0 
n2 = 1
count = 0
if n <= 0:
    print("Please enter positive number")
"""
elif n == 1:
    print("Fibonacci series upto " , n )
    print(n1)
"""
else:
    print("Fibonacci series upto " , n )
    while(count < n):
        
        print(n1)
        temp = n1 + n2
        n1 = n2
        n2 = temp
        count += 1

