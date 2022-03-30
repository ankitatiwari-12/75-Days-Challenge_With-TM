class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        wstart=0
        ans=0
        wsum=0
        total=sum(cardPoints)
        for wend in range(len(cardPoints)):
            wsum+=cardPoints[wend]
            if wend-wstart+1 >len(cardPoints)-k:
                wsum-=cardPoints[wstart]
                wstart+=1
            if wend-wstart+1 == len(cardPoints)-k:
                ans=max(ans,total-wsum)
            #print(ans )
        return ans