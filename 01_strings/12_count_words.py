# Question:
# Count the number of words in a sentence.

text = input("Enter a sentence: ")


# Method 1: Using split()
words = text.split()
count = len(words)

print("Method 1:")
print("Number of words:", count)


# Method 2: Using a loop
count = 0
in_word = False

for char in text:
    if not char.isspace():
        if not in_word:
            count += 1
            in_word = True
    else:
        in_word = False

print("Method 2:")
print("Number of words:", count)