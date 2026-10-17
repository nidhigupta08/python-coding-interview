# Question:
# Find the index of a target element using Linear Search.

nums = [10, 25, 30, 45, 50]
target = 30


# Method 1: Using a for loop
found = False

for i in range(len(nums)):
    if nums[i] == target:
        print("Method 1:")
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Method 1: Element not found")


# Method 2: Using a while loop
i = 0
found = False

while i < len(nums):
    if nums[i] == target:
        print("Method 2:")
        print("Element found at index:", i)
        found = True
        break

    i += 1

if not found:
    print("Method 2: Element not found")


# Method 3: Using the built-in index() method
print("Method 3:")

if target in nums:
    print("Element found at index:", nums.index(target))
else:
    print("Element not found")