def numIdenticalPairs(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        for i in range(len(nums)-1):            #0 - 4
            for j in range(i+1,len(nums))  :     #1 - 5
                if nums[i] == nums[j]:
                    num+=1
                    
        return num



print(numIdenticalPairs([1,2,3,1,1,3]))

