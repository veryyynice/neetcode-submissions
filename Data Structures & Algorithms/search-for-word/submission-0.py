class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        ROWS, COLS = len(board),len(board[0])
        def dfs(y,x, i): #want to mutate original array for visited matrix
            if i == len(word):
                return True
            if y < 0 or x < 0 or y>= ROWS or x >= COLS or board[y][x] == 1 or word[i] != board[y][x] or board[y][x] == "#":
                return
            

            #i.append(board[y][x])
            board[y][x] = "#"
            res = (dfs(y + 1, x, i + 1) or
                   dfs(y - 1, x, i + 1) or
                   dfs(y, x + 1, i + 1) or
                   dfs(y, x - 1, i + 1))            
            board[y][x] = word[i]
            #i.pop()
            return res
        for y in range(ROWS):
            for x in range(COLS):
                if board[y][x] == word[0]:
                    if dfs(y,x, 0) == True:
                        return True
        return False