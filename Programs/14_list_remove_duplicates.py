"""
Question: Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
Extras:
    1.Write two different functions to do this - one using a loop and constructing a list, and another using sets.
    2.Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

import random as r
l = r.choices(range(1,9), k=10)
print(sorted(l))
def no_duplicates(l):
    ndl = []
    for i in l:
        if i not in ndl:
            ndl.append(i)
    return sorted(ndl)

def no_duplicates_set(l):
    return list(set(l))

print(f"No duplicates: {no_duplicates(l)}")
print(f"No duplicates using Set: {no_duplicates_set(l)}")