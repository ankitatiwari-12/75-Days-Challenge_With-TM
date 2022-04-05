class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        rind=nser(h) 
        lind=nsel(h)
        max_area=0
        for i in range(len(h)):
            max_area=max(max_area,h[i]*(rind[i]-lind[i]-1))
        return max_area
def nser(arr):
    ans=[]
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        while len(stack)>0 and arr[stack[-1]]>=arr[i]:
            stack.pop()
        if len(stack)>0:
            ans.append(stack[-1])
        else:
            ans.append(len(arr))
        stack.append(i)
    ans.reverse()
    return ans
def nsel(arr):
    ans=[]
    stack=[]
    for i in range(len(arr) ):
        while len(stack)>0 and arr[stack[-1]]>=arr[i]:
            stack.pop()
        if len(stack)>0:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(i)
    return ans