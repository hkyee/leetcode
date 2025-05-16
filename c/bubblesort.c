#include <stdio.h>

void bubbleSort(int list[], int n);

int main(void)
{
    int listTest[7] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(listTest) /
            sizeof(listTest[0]); // Array Decay, so must be out of function
    bubbleSort(listTest, n);
}

void bubbleSort(int list[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 1; j < n - i; j++)
        {
            if (list[j] < list[j - 1])
            {
                int tmp = list[j];
                list[j] = list[j - 1];
                list[j - 1] = tmp;
            }
        }
    }

    // Print the array
    for (int i = 0; i < n; i++)
    {
        printf("%i, ", list[i]);
    }
}
