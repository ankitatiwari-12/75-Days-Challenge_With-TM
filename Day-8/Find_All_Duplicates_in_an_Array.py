class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        ans=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i]==2:
                ans.append(i)
        return ans