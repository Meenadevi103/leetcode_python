class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        count=0
        p=1
        j=0
        for i in range(len(nums)):
            p=p*nums[i]
            while(p>=k):
                
                p=p//nums[j]
                j+=1
            count+=(i-j)+1
        return count
    