# Question:
# Move all zeros to the end of an array
# while preserving the order of non-zero elements.

nums = [0, 1, 0, 3, 12]


# Method 1: Using a new list
result = []

for num in nums:
    if num != 0:
        result.append(num)

zero_count = len(nums) - len(result)

for i in range(zero_count):
    result.append(0)

print("Method 1:")
print(result)


# Method 2: Using list comprehensions
result = [num for num in nums if num != 0]
result += [0] * nums.count(0)

print("Method 2:")
print(result)


# Method 3: Using two pointers (in-place)
result = nums.copy()
position = 0

for i in range(len(result)):
    if result[i] != 0:
        result[position] = result[i]
        position += 1

while position < len(result):
    result[position] = 0
    position += 1

print("Method 3:")
print(result)