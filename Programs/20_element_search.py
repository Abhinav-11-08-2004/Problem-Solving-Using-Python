"""
Question: Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
Extras:
    1.Use binary search.
"""

def search(ordered_list, search_element):
    if search_element in ordered_list:
        return True
    else:
        return False
    
def iterative_binary_search(ordered_list, search_element):
    start_index = 0
    end_index = len(ordered_list) - 1

    while start_index <= end_index:
        
        middle_index = (start_index + end_index)//2
        
        if search_element==ordered_list[middle_index]:
            return f"{search_element} found at {middle_index} index"
        elif search_element < ordered_list[middle_index]:
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1
    return f"{search_element} not in list"

def recursive_binary_search(ordered_list, search_element, start_index, end_index):
    middle_index = (start_index + end_index)//2
    if start_index <= end_index:
        return f"{search_element} found at {middle_index} index"
    elif search_element < ordered_list[middle_index]:
        return recursive_binary_search(ordered_list, search_element, start_index, middle_index - 1)
    else:
        return recursive_binary_search(ordered_list, search_element, middle_index + 1, end_index)
 

#ordered_list = sorted(list(map(int, input("Enter the list elements: ").split())))
import random as r
ordered_list = sorted([i for i in r.choices(range(1,100), k=10)])
print(f"Ordered List: {ordered_list}")
search_element = int(input("Enter the search element: "))

#print(search(ordered_list, search_element))
#print(iterative_binary_search(ordered_list, search_element))
print(recursive_binary_search(ordered_list, search_element, 0, search_element))