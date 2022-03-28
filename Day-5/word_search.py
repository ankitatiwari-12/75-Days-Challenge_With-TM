class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction=[(-1,0),(0,-1),(0,1),(1,0)]
        visited=[[True]*len(board[0]) for _ in range(len(board))]
        queue=deque( )
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    queue.append((i,j,1))
                    visited[i][j]=False 
        i=1
        while queue :
            row,col,L=queue.popleft()
            print(row,col,L)
            for j,k in direction:
                nrow,ncol=row+j,col+k
                #print(visited)
                if not(nrow<0 or nrow>=len(board) or ncol<0 or ncol>=len(board[0]) or L>=len(word)) and board[nrow][ncol]==word[L] and visited[nrow][ncol]:
                    visited[nrow][ncol]=False
                    queue.append((nrow,ncol,L+1))
                    i=L+1
                    #break
            if L==len(word):
                return True
        return False
            