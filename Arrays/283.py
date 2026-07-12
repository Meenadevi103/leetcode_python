class Solution(object):
    def moveZeroes(self, nums):
        i=0
        j=0
        for j in range(len(nums)):
            if nums[j]!=0:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
        
        return nums
        