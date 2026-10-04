# Question:
# Write a Python program to find the character that occurs
# the most times in a given string.
#
# Example:
# Input: "banana"
# Output: "a"


text = input("Enter a string: ")


# Method 1: Using a dictionary with if-else
# Logic:
# First, count the frequency of each character.
# Then, find the character with the highest frequency.

counts = {}

for char in text:
    if char in counts:
        counts[char] = counts[char] + 1
    else:
        counts[char] = 1

most_frequent = None
highest_count = 0

for char in text:
    if counts[char] > highest_count:
        highest_count = counts[char]
        most_frequent = char

print("Method 1:")
print("Most frequent character:", most_frequent)


# Method 2: Using dictionary get()
# Logic:
# Use get() to count each character.
# Then use max() with the dictionary's get() method
# to find the character with the highest count.

counts = {}

for char in text:
    counts[char] = counts.get(char, 0) + 1

most_frequent = max(counts, key=counts.get)

print("Method 2:")
print("Most frequent character:", most_frequent)


# Method 3: Using Counter
# Logic:
# Counter automatically counts the frequency of each character.
# most_common(1) returns the character with the highest frequency.

from collections import Counter

counts = Counter(text)

most_frequent = counts.most_common(1)[0][0]

print("Method 3:")
print("Most frequent character:", most_frequent)