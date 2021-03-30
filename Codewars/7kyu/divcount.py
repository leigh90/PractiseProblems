# PROBLEM 6
# Count the number of divisors of a positive integer n.
# Random tests go up to n = 500000.

def divisors(n):
    divisible = []
    for i in range(1,n+1):
        if n % i == 0:
            divisible.append(i)
    print(len(divisible))


divisors(30)

