# Question: Sort an array using Insertion Sort.

nums = [5, 3, 8, 1, 2]
arr = nums.copy()
n = len(arr)

for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print("Insertion Sort:", arr)