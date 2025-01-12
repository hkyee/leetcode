#include <stdio.h>

void selectionSort(int list[], int n);
void swap(int list[], int i, int j);

int main(void)
{
    int listTest[7] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(listTest) / sizeof(listTest[0]);
    selectionSort(listTest, n);
}

void selectionSort(int list[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        int min_id = i;
        for (int j = 1 + i; j < n; j++)
        {
            if (list[j] < list[j - 1])
            {
                min_id = j;
            }
        }
        swap(list, i, min_id);
    }

    // Print the array
    for (int i = 0; i < n; i++)
    {
        printf("%i, ", list[i]);
    }
}

void swap(int list[], int i, int j)
{
    int tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
}
