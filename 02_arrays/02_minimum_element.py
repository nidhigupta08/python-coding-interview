# Question:
# Find the minimum element in an array
# without using Python's built-in min() function.

nums = [10, 5, 25, 3, 18]


# Method 1: Using for loop
minimum = nums[0]

for num in nums:
    if num < minimum:
        minimum = num

print("Method 1:")
print("Minimum element:", minimum)


# Method 2: Using while loop
minimum = nums[0]
i = 1

while i < len(nums):
    if nums[i] < minimum:
        minimum = nums[i]

    i += 1

print("Method 2:")
print("Minimum element:", minimum)


# Method 3: Using built-in min()
minimum = min(nums)

print("Method 3:")
print("Minimum element:", minimum)