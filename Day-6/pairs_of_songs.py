class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        remainder = {}
        for i in time:
            if i % 60 == 0 and 0 in remainder:
                ans += remainder[0]
            elif 60 - (i%60) in remainder:
                ans += remainder[60 - (i%60)]
            if i % 60 in remainder:
                remainder[i%60]+=1
            else:
                remainder[i%60]=1
        return ans