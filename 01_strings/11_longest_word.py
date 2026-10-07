# Question:
# Find the longest word in a given sentence.
#
# Example:
# Input: I am learning Python programming
# Output: programming


text = input("Enter a sentence: ")
words = text.split()


# Method 1: Using a for loop
max_length = 0
longest_word = ""

for word in words:
    current_length = len(word)

    if current_length > max_length:
        max_length = current_length
        longest_word = word

print("Method 1:")
print("Longest word:", longest_word)
print("Length:", max_length)


# Method 2: Using max() with key=len
longest_word = max(words, key=len)

print("Method 2:")
print("Longest word:", longest_word)
print("Length:", len(longest_word))


# Method 3: Using sorted()
longest_word = sorted(words, key=len, reverse=True)[0]

print("Method 3:")
print("Longest word:", longest_word)
print("Length:", len(longest_word))