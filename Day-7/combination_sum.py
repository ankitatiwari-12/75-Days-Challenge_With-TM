class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=list()
        def fun(n,s,res):
            if s==0:
                x=res[::-1]
                if x not in ans:
                    ans.append(x)
            if n==0 or  s<0:
                return 
            fun(n-1,s,res)
            res.append(candidates[n-1])
            fun(n,s-candidates[n-1],res)
            res.pop() 
        fun(len(candidates),target,[])
        return ans