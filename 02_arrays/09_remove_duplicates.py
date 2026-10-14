# Question:
# Remove duplicate elements from an array
# while preserving the original order.

nums = [1, 2, 3, 2, 4, 1, 5]


# Method 1: Using a for loop
unique = []

for num in nums:
    if num not in unique:
        unique.append(num)

print("Method 1:")
print("Array without duplicates:", unique)


# Method 2: Using a set to track seen elements
unique = []
seen = set()

for num in nums:
    if num not in seen:
        unique.append(num)
        seen.add(num)

print("Method 2:")
print("Array without duplicates:", unique)


# Method 3: Using dict.fromkeys()
unique = list(dict.fromkeys(nums))

print("Method 3:")
print("Array without duplicates:", unique)