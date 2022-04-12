# Problem No 2 : sum of all odd numbers using function

def sum_of_odd (n):
    sum = 0
    for i in range(1,n+1,2):
        sum = sum + i
    print("sum of odd numbers:",sum)

n = int(input("Enter n value:"))
sum_of_odd(n)



