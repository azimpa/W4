def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 4

position = linear_search(arr, target)

if position != -1:
    print("Value found at position", position + 1)
else:
    print("Value not found")
