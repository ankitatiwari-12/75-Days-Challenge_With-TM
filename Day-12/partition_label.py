class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        ans=[]
        for i in range(len(s)):
            d[s[i]]=i
        j=0
        partition=0
        for i in range(len(s)):
            j=max(j,d[s[i]])
            
            if i==j:
                part=i-partition+1
                partition=i+1
                ans.append(part)
        return ans
                