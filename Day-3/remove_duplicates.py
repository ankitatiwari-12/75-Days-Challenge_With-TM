class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        j=0
        for i in range(1,len(nums)):
            if nums[i]==nums[j]:
                nums[i]='_'
            else:
                key=nums[i]
                nums[i]='_'
                nums[j+1]=key
                j+=1
                k+=1
        return k