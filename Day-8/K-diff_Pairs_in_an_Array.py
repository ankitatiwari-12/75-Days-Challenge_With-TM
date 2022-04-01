class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if len(nums) == 0 or k < 0:  
            return 0 

        Map ={ }
        count = 0 
        for i in nums:
            Map[i]= Map.get(i, 0) + 1 

        for i in Map:
            if (k == 0): 
                if (Map[i] >= 2) :
                    count+=1 
            else:
                if i + k in Map:
                    count+=1 
        return count 