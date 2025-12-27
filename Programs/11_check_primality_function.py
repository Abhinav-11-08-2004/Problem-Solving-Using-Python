"""
Question: Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you."""

def prime(n):
    for i in range(2,(n+1)//2):
        if n%i==0:
            return f"{n} is not prime!"
    return f"{n} is prime!"

n = int(input("Number: "))
print(prime(n))