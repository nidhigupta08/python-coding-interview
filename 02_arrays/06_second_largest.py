# Question:
# Find the second largest distinct element in an array.

nums = [10, 20, 5, 40, 30]


# Method 1: Using a for loop
largest = float("-inf")
second_largest = float("-inf")

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Method 1:")
if second_largest == float("-inf"):
    print("Second largest element does not exist")
else:
    print("Second largest element:", second_largest)


# Method 2: Using a set and sorted()
unique_nums = sorted(set(nums), reverse=True)

print("Method 2:")
if len(unique_nums) < 2:
    print("Second largest element does not exist")
else:
    print("Second largest element:", unique_nums[1])


# Method 3: Using a set and max()
unique_nums = set(nums)

print("Method 3:")
if len(unique_nums) < 2:
    print("Second largest element does not exist")
else:
    largest = max(unique_nums)
    unique_nums.remove(largest)
    second_largest = max(unique_nums)
    print("Second largest element:", second_largest)