# Problem no 3: Write a program to check if a given number is perfect or not.
def all_divisor(num):
    sum = 0
    for i in range(1,num):
        if (num % i == 0):
            sum = sum + i

    if (sum == num):
        print(num,"is perfect number.")
    else:
        print(num,"is not perfect number")

num = int(input("Enter a number:"))
all_divisor(num)