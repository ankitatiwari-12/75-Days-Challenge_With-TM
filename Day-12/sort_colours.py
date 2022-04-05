class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d={0:0,1:0,2:0}
        for i in nums:
            d[i]+=1
        u=0
        for i in range(len(nums)):
            while d[u]==0:
                u+=1
            nums[i]=u
            d[u]-=1
        return