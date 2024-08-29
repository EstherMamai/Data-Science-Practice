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


