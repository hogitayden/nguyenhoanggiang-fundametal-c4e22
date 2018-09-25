# n = int(input("Enter your number, "))
# import math
# n = math.factorial(n)
# print("n! = ",n)

n = int(input("Enter your number, "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = factorial(n)
print("n! = ",n)