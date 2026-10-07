# Question:
# Find the sum of all elements in an array.

nums = [10, 20, 30, 40, 50]


# Method 1: Using for loop
total = 0

for num in nums:
    total = total + num

print("Method 1:")
print("The sum of the array is:", total)


# Method 2: Using while loop
total = 0
i = 0

while i < len(nums):
    total = total + nums[i]
    i += 1

print("Method 2:")
print("The sum of the array is:", total)


# Method 3: Using built-in sum()
total = sum(nums)

print("Method 3:")
print("The sum of the array is:", total)