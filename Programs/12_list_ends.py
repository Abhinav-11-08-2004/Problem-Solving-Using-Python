"""
Question: Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
"""

import random as r
l = r.choices(range(1,11), k=10)
print(l)
'''print([l[i] for i in range(len(l)) if i==0 or i==len(l)-1])'''

# Using indexing
'''le = l.pop()
fe = l[-(len(l))]
nl = []
nl.append(fe)
nl.append(le)
print(nl)'''

# nl = [l[0], l[-1]]
# nl = [l[-(len(l))], l[-1]]


# Using slicing 
list_lenght = len(l)
nl = l[::list_lenght-1]
print(nl)