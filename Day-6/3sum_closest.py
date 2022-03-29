class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:  
        nums.sort()
        mindiff=math.inf
        closestsum=0
        for i in range(len(nums)-2):
            t=target-nums[i]
            j=i+1
            k=len(nums)-1
            while j< k:
                sum1=nums[j]+nums[k]
                diff=abs(sum1-t)
                if diff<mindiff:
                    mindiff=diff
                    closestsum=sum1+nums[i]
                if sum1<t:
                    j+=1
                else:
                    k-=1
        return closestsum