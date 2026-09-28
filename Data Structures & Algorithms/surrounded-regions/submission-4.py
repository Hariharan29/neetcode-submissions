class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board),len(board[0])

        q =deque()

        def bfs(r,c):
            if (r<0 or c<0 or r==ROW or c== COL or board[r][c]!='O'):
                return
            q.append([r,c])
            board[r][c]='T'

            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if (nr<0 or nc<0 or nr==ROW or nc== COL  or board[nr][nc]!='O'):
                        continue
                    q.append([nr,nc])
                    board[nr][nc]='T'


        for c in range(COL):
            bfs(0,c)
            bfs(ROW-1,c)
        for r in range(ROW):
            bfs(r,0)
            bfs(r,COL-1)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='T':
                    board[r][c]='O'

        
        