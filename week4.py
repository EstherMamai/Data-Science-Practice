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