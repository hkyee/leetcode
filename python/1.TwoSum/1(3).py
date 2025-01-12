'''
User inputs a list of numbers, and a target
Output the index of 2 numbers in the list which is equal to the target
'''





A = map(int,input("Enter a list of numbers separated with spaces \n").split())
A = list(A)

target = int(input("Enter your sum target\n"))

seen = {}

def twoSum(nums, target):
    for i,num in enumerate(A):
        if target - num in seen:
            print(seen)
            return ([seen[target - num] , i])
            
        elif num not in seen:
            seen[num] = i
    

print(twoSum(A,target))

'''
This code checks whether the target subtracted from the current checked number is in seen, if not add it to seen
'''
