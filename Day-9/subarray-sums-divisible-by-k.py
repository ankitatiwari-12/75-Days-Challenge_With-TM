class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        psum=0
        visited=defaultdict(int)
        visited[ 0]=1 
        for j in range(n):
            psum =(psum+nums[j])%k
            #print(visited)
            #print(psum-k)
            if psum<0:
                psum+=k
        
            count+=visited[psum ]
            visited[psum]+=1
        return count