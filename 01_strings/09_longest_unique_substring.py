text = input("Enter a string: ")


# Using a set and a sliding window
# Logic:
# Use a set to store characters in the current window.
# If a duplicate character is found, remove characters from
# the beginning of the window until the duplicate is removed.
# Keep track of the maximum window length.

seen = set()
left = 0
max_length = 0

for right in range(len(text)):
    while text[right] in seen:
        seen.remove(text[left])
        left += 1

    seen.add(text[right])

    current_length = right - left + 1

    if current_length > max_length:
        max_length = current_length

print("Longest substring length:", max_length)