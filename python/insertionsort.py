# InsertionSort

# Similar to sorting playing cards
# It inserts a number into its correct position by shifting larger number to the right.


def insertionSort(list):
    N = len(list)

    for i in range(1, N):
        key = list[i]
        j = i - 1  # Compare with previous number
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1  # Decrement j to compare with the element before
        list[j + 1] = key

        # We add 1 because if not it would be -1, or would be a position behind due to j-=1 in while loop.

    return list


listTest = [12, 11, 13, 5, 6]

print(insertionSort(listTest))
