# Problem No 4 : fibonacci series

def fibonacci_series ():
    a = 1
    b = 0
    for i in range(1,n+1):
        c = a + b
        print(c,end=" ")
        a = b
        b = c

n = int(input("Enter value:"))
fibonacci_series()
