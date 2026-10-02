# Question:
# Write a Python program to check whether a given string is a palindrome.
#
# A palindrome is a string that reads the same forward and backward.


text = input("Enter a string: ")


# Method 1: Using negative indexing
# Logic: Start from the last character (-1) and move backward
# through the string using a negative step.

reverse = ""

for i in range(-1, -len(text) - 1, -1):
    reverse = reverse + text[i]

if text == reverse:
    print("Method 1: Given text is a palindrome")
else:
    print("Method 1: Given text is not a palindrome")


# Method 2: Using string slicing
# Logic: [::-1] reverses the string using a step of -1.

reverse = text[::-1]

if text == reverse:
    print("Method 2: Given text is a palindrome")
else:
    print("Method 2: Given text is not a palindrome")


# Method 3: Using a for loop
# Logic: Add each character to the beginning of the result string
# to create the reversed string.

reverse = ""

for char in text:
    reverse = char + reverse

if text == reverse:
    print("Method 3: Given text is a palindrome")
else:
    print("Method 3: Given text is not a palindrome")