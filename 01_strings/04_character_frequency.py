# Question:
# Write a Python program to count the frequency of each character
# in a given string.
#
# Example:
# Input: "hello"
# Output:
# h: 1
# e: 1
# l: 2
# o: 1


text = input("Enter a string: ")


# Method 1: Using a dictionary with if-else
# Logic:
# Create an empty dictionary to store each character and its count.
# If the character already exists in the dictionary, increase its count.
# Otherwise, add the character with a count of 1.

counts = {}

for char in text:
    if char in counts:
        counts[char] = counts[char] + 1
    else:
        counts[char] = 1

print("Method 1:")
print(counts)


# Method 2: Using dictionary get()
# Logic:
# get() returns the current count of the character.
# If the character does not exist, get() returns 0.
# Then increase the value by 1.

counts = {}

for char in text:
    counts[char] = counts.get(char, 0) + 1

print("Method 2:")
print(counts)


# Method 3: Using Counter
# Logic:
# Counter is provided by Python's collections module.
# It automatically counts how many times each character occurs.

from collections import Counter

counts = Counter(text)

print("Method 3:")
print(counts)