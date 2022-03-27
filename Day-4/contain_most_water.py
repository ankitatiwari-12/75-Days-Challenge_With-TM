class Solution:
    def maxArea(self, h: List[int]) -> int:
        i=0
        j=len(h)-1
        maxarea=0
        while i<j:
            maxarea=max(maxarea,min(h[i],h[j])*(j-i))
            if h[i]<h[j]:
                i+=1
            else:
                j-=1
        return maxarea
        maxarea=0
        for i in range(len(h)):
            for j in range(i+1,len(h)):
                maxarea=max(maxarea,min(h[i],h[j])*(j-i))
        return maxarea