# Problem no 6: Write a program to check if given number is perfect square or not.
import math
def sqrt ():
    x = int(math.sqrt(num))
    if (num == x**2):
        print(num,"is perfect square of",x)
    else:
        print(num,"is not perfect square")

num = int(input("Enter a number:"))
sqrt()