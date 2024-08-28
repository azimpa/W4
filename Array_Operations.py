# unique elements
def find_unique_elements(arr):
    unique_elements = set()
    for element in arr:
        unique_elements.add(element)
    return list(unique_elements)


my_array = [1, 2, 3, 4, 1, 2, 5, 6, 3, 4, 7, 8, 5]
unique_elements = find_unique_elements(my_array)
print("Unique elements:", unique_elements)


# reversing elements
def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)  # Output: [5, 4, 3, 2, 1]


# reversing string
def reverse_string(s):
    reversed_string = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    return reversed_string


s = "hello"
reversed_s = reverse_string(s)
print(reversed_s)  # Output: "olleh"


# inserting elements
def insert_value(array, index, value):
    array.append(None)

    for i in range(len(array) - 1, index, -1):
        array[i] = array[i - 1]

    array[index] = value


my_array = [1, 2, 3, 4, 5]
insert_value(my_array, 2, 10)
print(my_array)


# deleting elements
def delete_element(arr, index):
    new_arr = [None] * (len(arr) - 1)

    j = 0
    for i in range(len(arr)):
        if i != index:
            new_arr[j] = arr[i]
            j += 1

    return new_arr


my_array = [1, 2, 3, 4, 5]
index_to_delete = 2
result_array = delete_element(my_array, index_to_delete)
print(result_array)


# merge sorted
def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10]
result = merge_sorted_arrays(arr1, arr2)
print(result)


# merge unsorted
def merge_arrays(arr1, arr2):
    merged_arr = arr1 + arr2

    return merged_arr


array1 = [5, 2, 1]
array2 = [7, 4, 6]

merged_array = merge_arrays(array1, array2)
print(merged_array)
