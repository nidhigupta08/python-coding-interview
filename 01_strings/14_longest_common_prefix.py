# Question:
# Find the longest common prefix among strings.

words = ["flower", "flow", "flight"]


# Method 1: Using a loop
prefix = words[0]

for word in words[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

        if prefix == "":
            break

print("Method 1:")
print("Longest common prefix:", prefix)


# Method 2: Using sorting
sorted_words = sorted(words)
first = sorted_words[0]
last = sorted_words[-1]

prefix = ""

for i in range(min(len(first), len(last))):
    if first[i] == last[i]:
        prefix += first[i]
    else:
        break

print("Method 2:")
print("Longest common prefix:", prefix)