# Question:
# Find the maximum element in an array
# without using Python's built-in max() function.

nums = [10, 25, 7, 42, 18]


# Method 1: Using for loop
maximum = nums[0]

for num in nums:
    if num > maximum:
        maximum = num

print("Method 1:")
print("Maximum element:", maximum)


# Method 2: Using while loop
maximum = nums[0]
i = 1

while i < len(nums):
    if nums[i] > maximum:
        maximum = nums[i]

    i += 1

print("Method 2:")
print("Maximum element:", maximum)


# Method 3: Using built-in max()
maximum = max(nums)

print("Method 3:")
print("Maximum element:", maximum)