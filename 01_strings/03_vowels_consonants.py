# Question:
# Write a Python program to count the number of vowels and consonants
# in a given string.
#
# Spaces, numbers, and special characters should not be counted.
#
# Example:
# Input: "hello world! 123"
# Output:
# Vowels: 3
# Consonants: 7


text = input("Enter a string: ")


# Method 1: Using 'in' with a string
# Logic:
# First check whether the character is an alphabet.
# If it is an alphabet, check whether it is present in "aeiou".
# If it is present, count it as a vowel.
# Otherwise, count it as a consonant.

vowels = 0
consonants = 0

for char in text:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Method 1:")
print("Vowels:", vowels)
print("Consonants:", consonants)


# Method 2: Using a set of vowels
# Logic:
# Store the vowels in a set.
# Check whether each alphabet character is present in the set.
# If present, count it as a vowel.
# Otherwise, count it as a consonant.

vowels = 0
consonants = 0
vowels_set = {"a", "e", "i", "o", "u"}

for char in text:
    if char.isalpha():
        if char.lower() in vowels_set:
            vowels += 1
        else:
            consonants += 1

print("Method 2:")
print("Vowels:", vowels)
print("Consonants:", consonants)


# Method 3: Using logical OR conditions
# Logic:
# Check whether the character is one of the five vowels
# using logical OR conditions.
# If it is a vowel, increase the vowel count.
# Otherwise, if it is an alphabet, increase the consonant count.

vowels = 0
consonants = 0

for char in text:
    char = char.lower()

    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        vowels += 1
    elif char.isalpha():
        consonants += 1

print("Method 3:")
print("Vowels:", vowels)
print("Consonants:", consonants)