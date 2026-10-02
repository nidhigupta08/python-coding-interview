# Question:
# Write a Python program to reverse a given string without using
# Python's built-in reversed() function.


# Method 1: Using a for loop
# Logic: Add each character to the beginning of the result string.

text = "hello"
result = ""

for char in text:
    result = char + result

print("Method 1:", result)


# Method 2: Using negative indexing
# Logic: Start from the last character (-1) and move backward
# through the string using a negative step.

text = "hello"
reverse = ""

for i in range(-1, -6, -1):
    reverse = reverse + text[i]

print("Method 2:", reverse)


# Method 3: Using string slicing
# Logic: [::-1] traverses the string backward with a step of -1.

text = "hello"

sliced_reverse = text[::-1]

print("Method 3:", sliced_reverse)