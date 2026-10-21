# Question: Sort an array using Bubble Sort.

nums = [5, 3, 8, 1, 2]
arr = nums.copy()
n = len(arr)

for i in range(n):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Bubble Sort:", arr)