# Question:
# Find the index of a target element using Binary Search.
# The array must be sorted in ascending order.

nums = [10, 20, 30, 40, 50, 60, 70]
target = 50


# Method 1: Using a while loop
left = 0
right = len(nums) - 1
found_index = -1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        found_index = mid
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print("Method 1:")
if found_index != -1:
    print("Element found at index:", found_index)
else:
    print("Element not found")


# Method 2: Using recursion
def binary_search(nums, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search(nums, mid + 1, right, target)
    else:
        return binary_search(nums, left, mid - 1, target)


result = binary_search(nums, 0, len(nums) - 1, target)

print("Method 2:")
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")


# Method 3: Using the bisect module
from bisect import bisect_left

index = bisect_left(nums, target)

print("Method 3:")
if index < len(nums) and nums[index] == target:
    print("Element found at index:", index)
else:
    print("Element not found")