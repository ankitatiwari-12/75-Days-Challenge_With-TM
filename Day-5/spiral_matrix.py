class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiralMatrixPrint(row, col, arr): 
            top = 0
            bottom = row-1
            left = 0
            right = col - 1 
            dir = 0
            ans=[]
            while (top <= bottom and left <=right):    
                if dir ==0:
                    for i in range(left,right+1): 
                        ans.append(arr[top][i] ) 
                    top +=1
                    dir = 1

                elif dir ==1:
                    for i in range(top,bottom+1): 
                        ans.append(arr[i][right] ) 
                    right -=1 
                    dir = 2

                elif dir ==2:
                    for i in range(right,left-1,-1): 
                        ans.append(arr[bottom][i] ) 
                    bottom -=1
                    dir = 3

                elif dir ==3:
                    for i in range(bottom,top-1,-1): 
                        ans.append(arr[i][left] ) 
                    left +=1
                    dir = 0 
            return ans
        return spiralMatrixPrint(len(matrix),len(matrix[0]),matrix)