class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #nums.sort()
        k=len(nums)
        for i in range(k):
            while nums[i]!=i+1:
                if nums[i]<=0 or nums[i]>=k:
                    break
                if nums[i]==nums[nums[i]-1]:
                    break
                temp = nums[i]
                nums[i],nums[temp-1] = nums[temp - 1],temp
                #nums[temp - 1] = temp
        for i in range(k):
            if nums[i]!=i+1:
                return i+1
        return k+1
    
    
    
    