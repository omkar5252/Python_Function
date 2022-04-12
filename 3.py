# Problem No 2 : sum of all prime numbers using function.

def sum_of_prime_numbers():
    sum = 0
    for i in range(1,n+1):
        for j in range(2,i):
            if (i % j == 0):
                break
        else:
            sum = sum + i
    print("sum of prime numbers:",sum)

n = int(input("Enter n value:"))
sum_of_prime_numbers()

        