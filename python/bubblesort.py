# BubbleSort

# Compare adjacent items
# Highest number will bubble to the right with each iteration
# Sorted list will form at the end of the array


def bubbleSort(list):
    N = len(list)
    for i in range(0, N - 1):  # i loop controls the iteration through the list.
        for j in range(1, N - i):  # j loop controls the comparison and swapping.
            if list[j] < list[j - 1]:
                tmp = list[j - 1]
                list[j - 1] = list[j]
                list[j] = tmp

    return list


# listTest = [3, 2, 5, 4, 1]
listTest = [64, 34, 25, 12, 22, 11, 90]

print(bubbleSort(listTest))


# Time complexity = 0(n^2)
