class Solution:
    def maxAreaOfIsland(self, matrix: List[List[int]]) -> int:
        ROW=len(matrix)
        COL=len(matrix[0])
        def isSafe(M, row, col, visited):
            #global ROW, COL 
            return ((row >= 0) and (row < ROW) and (col >= 0) and (col < COL) and (M[row][col] and not visited[row][col])) 
        def DFS(M, row, col, visited, count): 
            rowNbr = [-1, 1, 0, 0]
            colNbr = [0, 0, -1, 1] 
            visited[row][col] = True 
            for k in range(4):
                if (isSafe(M, row + rowNbr[k], col + colNbr[k], visited)): 
                    count[0] += 1
                    DFS(M, row + rowNbr[k], col + colNbr[k], visited, count) 
        def largestRegion(M):
            #global ROW, COL 
            visited = [[0] * COL for i in range(ROW)] 
            result =  0
            for i in range(ROW):
                for j in range(COL): 
                    if (M[i][j] and not visited[i][j]): 
                        count = [1]
                        DFS(M, i, j, visited, count) 
                        result = max(result, count[0])
            return result 
        return largestRegion(matrix)