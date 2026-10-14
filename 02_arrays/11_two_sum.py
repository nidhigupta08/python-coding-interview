# Question:
# Find two numbers whose sum equals the target.

nums = [2, 7, 11, 15]
target = 9


# Method 1: Using nested loops
found = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print("Method 1:")
            print("Numbers:", nums[i], "and", nums[j])
            found = True
            break
    if found:
        break

if not found:
    print("Method 1: No pair found")


# Method 2: Using a set
seen = set()
found = False

for num in nums:
    complement = target - num

    if complement in seen:
        print("Method 2:")
        print("Numbers:", complement, "and", num)
        found = True
        break

    seen.add(num)

if not found:
    print("Method 2: No pair found")


# Method 3: Using a dictionary
seen = {}
found = False

for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        print("Method 3:")
        print("Numbers:", complement, "and", num)
        print("Indexes:", seen[complement], "and", i)
        found = True
        break

    seen[num] = i

if not found:
    print("Method 3: No pair found")