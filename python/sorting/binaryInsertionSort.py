def binary_search(arr, val, start, end):

    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1
    if start > end:
        return start
    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]

        j = binary_search(arr, key, 0, i - 1)
        # Position the key, skipping arr[i]
        arr = arr[:j] + [key] + arr[j:i] + arr[i + 1 :]
    return arr


listTest = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(listTest))
