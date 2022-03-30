class Solution:
    def jump(self, nums: List[int]) -> int:
        #count=0
        mincount=0 
        i=0
        curr=-1
        next=0 
        while next < len(nums)-1:
            if i > curr:
                mincount += 1
                curr = next
            next = max(next, nums[i] + i)
            i += 1
        return mincount
         