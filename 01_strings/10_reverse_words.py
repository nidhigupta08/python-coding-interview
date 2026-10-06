# Question:
# Write a Python program to reverse the order of words in a sentence.
#
# The words themselves should not be reversed.
#
# Example:
# Input: "I love Python"
# Output: "Python love I"


text = input("Enter a sentence: ")


# Method 1: Using split(), slicing, and join()
# Logic:
# split() separates the sentence into individual words.
# [::-1] reverses the order of the words.
# join() combines the reversed words into a sentence.

words = text.split()

words = words[::-1]

result = " ".join(words)

print("Method 1:")
print("Reversed sentence:", result)


# Method 2: Using split(), reverse(), and join()
# Logic:
# split() separates the sentence into individual words.
# reverse() reverses the list in place.
# join() combines the words back into a sentence.

words = text.split()

words.reverse()

result = " ".join(words)

print("Method 2:")
print("Reversed sentence:", result)


# Method 3: Using a for loop
# Logic:
# split() separates the sentence into individual words.
# Add each word to the beginning of the result.
# This reverses the order of the words.
# strip() removes the extra space at the beginning or end.

words = text.split()

result = ""

for word in words:
    result = word + " " + result

result = result.strip()

print("Method 3:")
print("Reversed sentence:", result)