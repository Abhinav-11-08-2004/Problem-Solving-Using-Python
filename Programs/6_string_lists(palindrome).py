"""
Question: Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

s = input("String: ")
if s == s[::-1]:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")