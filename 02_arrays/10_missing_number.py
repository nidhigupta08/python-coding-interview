# Question:
# Find the missing number from numbers 1 to n.
# Exactly one number is missing.

nums = [1, 2, 4, 5]
n = len(nums) + 1


# Method 1: Using the sum formula
expected_sum = n * (n + 1) // 2
actual_sum = 0

for num in nums:
    actual_sum += num

missing = expected_sum - actual_sum

print("Method 1:")
print("Missing number:", missing)


# Method 2: Using a set
numbers_set = set(nums)
missing = None

for num in range(1, n + 1):
    if num not in numbers_set:
        missing = num
        break

print("Method 2:")
print("Missing number:", missing)


# Method 3: Using XOR
missing = 0

for num in range(1, n + 1):
    missing ^= num

for num in nums:
    missing ^= num

print("Method 3:")
print("Missing number:", missing)