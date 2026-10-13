# Question:
# Find duplicate elements in an array.

nums = [1, 2, 3, 2, 4, 5, 1]


# Method 1: Using nested for loops
duplicates = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j] and nums[i] not in duplicates:
            duplicates.append(nums[i])

print("Method 1:")
print("Duplicate elements:", duplicates)


# Method 2: Using a set
seen = set()
duplicates = []

for num in nums:
    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.add(num)

print("Method 2:")
print("Duplicate elements:", duplicates)


# Method 3: Using count()
duplicates = []

for num in nums:
    if nums.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Method 3:")
print("Duplicate elements:", duplicates)