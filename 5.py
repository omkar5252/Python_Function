# Problem no 5: Write a program to check if a given number is Fibonacci number.
def fibo(num):
    c = 0
    a = 1
    b = 1
    if (num == 0 or num ==1):
        print("Given number is in fibo series.")
    else:
        while (c < num):
            c = a + b
            a = b
            b = c

        if (num == c):
            print("Given number is in fibo series")
        else:
            print("Given number is not in fibo series")

num = int(input("Enter a number:"))
fibo(num)