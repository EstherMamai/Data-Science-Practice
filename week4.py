#1. Checking if a string is a palindrome using a stack
def is_palindrome(s):
    stack = []
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Create a reversed string using the stack
    reversed_s = ""
    while stack:
        reversed_s += stack.pop()
    
    # Check if the original string is the same as the reversed string
    return s == reversed_s

# Example usage:
print(is_palindrome("radar"))
print(is_palindrome("hello"))  
print(is_palindrome("teapot"))

"""List Comprehension
List comprehension is a concise way to create lists in Python. 
It allows for generating a new list by applying an expression to each item in an existing iterable."""

#1. Basic list
squares = [x**2 for x in range(10)]
print(squares)  

#2. List comrehension with a condition
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers) 

#3. Nested List Comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)

"""
Compound Datatype in Python
A compound datatype is a datatype that can hold multiple values, possibly of different types.
"""
#Example 1: List. A list can hold multiple elements of different types.
my_list = [1, "hello", 3.14, [1, 2, 3]]
print(my_list)

#Example 2: Dictionary A dictionary holds key-value pairs, where each key maps to a specific value.
my_dict = {"name": "Alice", "age": 25, "is_student": True}
print(my_dict)

#Example 3: Tuple.  A tuple is an immutable sequence of elements, which can also be of different types.
my_tuple=(90, "Esther", 7.9)
print(my_tuple)

#Function to return a list of bigrams from a string
def get_bigrams(s):
    return [s[i:i+2] for i in range(len(s) - 1)]

print(get_bigrams("hello"))
