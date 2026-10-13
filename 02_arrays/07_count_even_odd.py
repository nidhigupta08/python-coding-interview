# Question:
# Count even and odd numbers in an array.

nums = [10, 15, 20, 25, 30, 7]

even_count = 0
odd_count = 0

for num in nums:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Method 1:")
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)


# Method 2: Using a while loop
even_count = 0
odd_count = 0
i = 0

while i < len(nums):
    if nums[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    i += 1

print("Method 2:")
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)


# Method 3: Using list comprehensions
even_count = len([num for num in nums if num % 2 == 0])
odd_count = len([num for num in nums if num % 2 != 0])

print("Method 3:")
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)