# Problem no 2: Write a program to print sum of all divisors of given number.
def sum_of_divsior(num):
    sum = 0
    for i in range(1,num+1):
        if (num % i == 0):
            sum = sum + i
    return sum

num = int(input("Enter a number:"))
result = sum_of_divsior(num)
print("sum of divisor:",result)