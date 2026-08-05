class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        #land is hortizontal or vertical
        ROWS, COLS = len(grid), len(grid[0])

        ans = 0
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(y,x):
            if min(int(y),int(x)) < 0 or y>= ROWS or x>= COLS or grid[y][x] == "0":
                return
            grid[y][x] = "0"
            for dir in directions:
                updated_y = y + dir[0]
                updated_x = x+ dir[1]
                dfs(updated_y,updated_x)
                

            return
            
        
        for r in range(ROWS):
            for c in range (COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    ans +=1
        return ans

