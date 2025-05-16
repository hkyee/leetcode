#include <stdio.h>

void insertionSort(int list[], int n);

int main(void)
{
    int listTest[7] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(listTest) / sizeof(listTest[0]);
    insertionSort(listTest, n);
}

void insertionSort(int list[], int n)
{
    for (int i = 1; i < n; i++)
    {
        int key = list[i];
        int j = i - 1;
        while ((j >= 0) && (key < list[j]))
        {
            list[j + 1] = list[j];
            j--;
        }
        list[j + 1] = key;
    }

    // Print Array
    for (int i = 0; i < n; i++)
    {
        printf("%i, ", list[i]);
    }
}
