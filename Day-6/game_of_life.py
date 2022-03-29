class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        kill=[]
        reproduce=[]
        directions=[(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1),(1,1)]
        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==0:
                    live_nei=0
                    for d in directions:
                        ni,nj=i+d[0],j+d[1]
                        if 0<=ni<m and 0<=nj<n and board[ni][nj]==1:
                            live_nei+=1
                    if live_nei==3:
                        reproduce.append((i,j))
                else:
                    live_nei=0
                    for d in directions:
                        ni,nj=i+d[0],j+d[1]
                        if 0<=ni<m and 0<=nj<n and board[ni][nj]==1:
                            live_nei+=1
                    if live_nei<2 or live_nei>3:
                        kill.append((i,j))
        for i,j in kill:
            board[i][j]=0
        for i,j in reproduce:
            board[i][j]=1
        """
        Do not return anything, modify board in-place instead.
        """
        