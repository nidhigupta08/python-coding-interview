# Question:
# Write a Python program to check whether two given strings are anagrams.
#
# Two strings are anagrams if they contain the same characters
# with the same frequencies, but in a different order.
#
# Example:
# Input:
# listen
# silent
#
# Output:
# The strings are anagrams


text1 = input("Enter the first string: ")
text2 = input("Enter the second string: ")


# Method 1: Using sorting
# Logic:
# Sort the characters of both strings.
# If the sorted strings are equal, the strings are anagrams.

if sorted(text1) == sorted(text2):
    print("Method 1: The strings are anagrams")
else:
    print("Method 1: The strings are not anagrams")


# Method 2: Using dictionaries
# Logic:
# Count the frequency of every character in both strings.
# If both dictionaries are equal, the strings are anagrams.

counts1 = {}
counts2 = {}

for char in text1:
    if char in counts1:
        counts1[char] = counts1[char] + 1
    else:
        counts1[char] = 1

for char in text2:
    if char in counts2:
        counts2[char] = counts2[char] + 1
    else:
        counts2[char] = 1

if counts1 == counts2:
    print("Method 2: The strings are anagrams")
else:
    print("Method 2: The strings are not anagrams")


# Method 3: Using Counter
# Logic:
# Counter automatically counts the frequency of each character.
# If both Counter objects are equal, the strings are anagrams.

from collections import Counter

counts1 = Counter(text1)
counts2 = Counter(text2)

if counts1 == counts2:
    print("Method 3: The strings are anagrams")
else:
    print("Method 3: The strings are not anagrams")