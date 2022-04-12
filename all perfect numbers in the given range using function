# Write a program to check to print all perfect numbers in the given range.
def apn(start,end):
    for n in range(start,end+1):
        sum = 0
        for i in range(1,n):
            if (n % i == 0):
                sum = sum + i

        if (n== sum):
            print(n,end=" ")

start = int(input("Enter a start number:"))
end = int(input("Enter a end number:"))

apn(start,end)


