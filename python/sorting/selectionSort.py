def selectionSort(list):
    n = len(list)

    for i in range(0, n - 1):
        min_idx = i
        for j in range(1 + i, n):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list


listTest = [64, 34, 25, 12, 22, 11, 90]

print(selectionSort(listTest))


# Time complexity
# (n - 1) + (n - 2) + (n - 3) + (n - 4) + .. + 1
# = n(n-1)/2
# O(n^2)
