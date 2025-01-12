'''
User inputs a list of numbers, and a target
Output the index of 2 numbers in the list which is equal to the target
'''





A = map(int,input("Enter a list of numbers separated with spaces \n").split())
A = list(A)

target = int(input("Enter your sum target\n"))


def twoSum(nums , target):

    for i in range(len(nums)-1):
        for j in range (i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
            

print(twoSum(A,target))


'''
Explanation

- This code runs 2 for loops
- i Loop starts from the first number, j Loop checks the following numbers until end of loop

'''