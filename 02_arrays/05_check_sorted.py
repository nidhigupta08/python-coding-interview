# Question:
# Check whether an array is sorted in ascending order.

nums = [10, 20, 30, 40, 50]


# Method 1: Using a for loop
is_sorted = True

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        is_sorted = False
        break

print("Method 1:")
if is_sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")


# Method 2: Using a while loop
is_sorted = True
i = 0

while i < len(nums) - 1:
    if nums[i] > nums[i + 1]:
        is_sorted = False
        break
    i += 1

print("Method 2:")
if is_sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")


# Method 3: Using sorted()
if nums == sorted(nums):
    print("Method 3:")
    print("Array is sorted")
else:
    print("Method 3:")
    print("Array is not sorted")