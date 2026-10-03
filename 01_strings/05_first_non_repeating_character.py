# Question:
# Write a Python program to find the first non-repeating character
# in a given string.
#
# A non-repeating character is a character that appears only once.
#
# Example:
# Input: "swiss"
# Output: "w"


text = input("Enter a string: ")


# Method 1: Using a dictionary with if-else
# Logic:
# First, count the frequency of every character.
# Then, go through the string again.
# The first character whose count is 1 is the first non-repeating character.

counts = {}

for char in text:
    if char in counts:
        counts[char] = counts[char] + 1
    else:
        counts[char] = 1

result = None

for char in text:
    if counts[char] == 1:
        result = char
        break

print("Method 1:")

if result is not None:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found")


# Method 2: Using dictionary get()
# Logic:
# Use get() to count the frequency of each character.
# Then traverse the original string again and find the first
# character whose frequency is 1.

counts = {}

for char in text:
    counts[char] = counts.get(char, 0) + 1

result = None

for char in text:
    if counts[char] == 1:
        result = char
        break

print("Method 2:")

if result is not None:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found")


# Method 3: Using Counter
# Logic:
# Counter automatically counts the frequency of each character.
# Then traverse the original string and find the first character
# whose count is 1.

from collections import Counter

counts = Counter(text)

result = None

for char in text:
    if counts[char] == 1:
        result = char
        break

print("Method 3:")

if result is not None:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found")