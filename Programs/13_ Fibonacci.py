"""
Question: Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

l = [0,1]
def fibonacci(n):
    nn = 1
    while(nn < n-1):
        l.append(l[nn-1]+l[nn])
        nn+=1
    return l

n = int(input("Number: "))
print(fibonacci(n))