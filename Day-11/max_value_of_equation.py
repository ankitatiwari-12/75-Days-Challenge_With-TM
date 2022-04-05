class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        
        ans=-math.inf
        maxheap=[]
        heappush(maxheap,(-(points[0][1] - points[0][0]),points[0][0]))
        
        for i in range(1,len(points)):
            while maxheap and points[i][0] - maxheap[0][1] > k:
                heappop(maxheap)
            
            if maxheap:
                ans=max(ans,points[i][1] + points[i][0] - maxheap[0][0])
            
            heappush(maxheap,(-(points[i][1] - points[i][0]),points[i][0]))       
        return ans
        
        
        