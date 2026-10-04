# Question:
# Write a Python program to remove duplicate characters
# from a given string.
#
# The first occurrence of each character should be preserved.
#
# Example:
# Input: "programming"
# Output: "progamin"


text = input("Enter a string: ")


# Method 1: Using a for loop and a string
# Logic:
# Create an empty string to store the result.
# Go through each character in the input.
# If the character is not already present in the result,
# add it to the result.

result = ""

for char in text:
    if char not in result:
        result = result + char

print("Method 1:")
print("String after removing duplicates:", result)


# Method 2: Using a set
# Logic:
# A set stores only unique values.
# Keep a separate set to remember characters that have
# already been seen.
# Add each character to the result only the first time it appears.

result = ""
seen = set()

for char in text:
    if char not in seen:
        result = result + char
        seen.add(char)

print("Method 2:")
print("String after removing duplicates:", result)


# Method 3: Using dict.fromkeys()
# Logic:
# Dictionaries preserve insertion order.
# dict.fromkeys() creates dictionary keys from the characters.
# Since dictionary keys must be unique, duplicate characters
# are automatically removed.
# join() converts the keys back into a string.

result = "".join(dict.fromkeys(text))

print("Method 3:")
print("String after removing duplicates:", result)