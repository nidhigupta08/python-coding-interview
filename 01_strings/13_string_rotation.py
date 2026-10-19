# Question:
# Check whether one string is a rotation of another.

text1 = input("Enter the first string: ")
text2 = input("Enter the second string: ")


# Method 1: Using concatenation and 'in'
if len(text1) == len(text2) and text2 in (text1 + text1):
    print("Method 1: Strings are rotations")
else:
    print("Method 1: Strings are not rotations")


# Method 2: Using a loop
is_rotation = False

if len(text1) == len(text2):
    for i in range(len(text1) + 1):
        rotated = text1[i:] + text1[:i]

        if rotated == text2:
            is_rotation = True
            break

print("Method 2:")
if is_rotation:
    print("Strings are rotations")
else:
    print("Strings are not rotations")