# Question:
# Reverse an array without using a built-in reverse() method.

nums = [10, 20, 30, 40, 50]


# Method 1: Using slicing
reverse = nums[::-1]

print("Method 1:")
print("Reversed array:", reverse)


# Method 2: Using a for loop
reverse = []

for i in range(len(nums) - 1, -1, -1):
    reverse.append(nums[i])

print("Method 2:")
print("Reversed array:", reverse)


# Method 3: Using built-in reverse()
reverse = nums.copy()  #to keep the original array 
reverse.reverse()  

print("Method 3:")
print("Reversed array:", reverse)