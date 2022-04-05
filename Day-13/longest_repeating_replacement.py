class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        wstart=0
        maxlen=maxlettercount=0
        d=dict()
        for wend in range(len(s)):
            d[s[wend]]=d.get(s[wend],0)+1
            maxlettercount=max(maxlettercount,d[s[wend]])
            if (wend-wstart+1-maxlettercount)>k:
                d[s[wstart]]-=1
                wstart+=1
            maxlen=max(maxlen,wend-wstart+1)
        return maxlen