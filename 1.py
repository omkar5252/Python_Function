# Problem no 1 : series of factorial using function

def series_of_factorial (n):
    fact = 1
    sum = 0
    for i in range(1,n+1):
        fact = fact * i
        sum = sum + fact
    return sum

n = int(input("Enter n value:"))
result = series_of_factorial(n)
print("series of factorial:",result)