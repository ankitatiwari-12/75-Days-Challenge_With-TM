class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        psum=0
        visited=defaultdict(int)
        visited[0]=1
        for j in range(len(nums)):
            psum+=nums[j]
            count+=visited[psum-k]
            visited[psum]+=1
        return count