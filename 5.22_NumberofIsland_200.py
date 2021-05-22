class Solution:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
        return islands
        
        
        
    def bfs(self, grid, x, y, visited):
        queue = collections.deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in self.DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                visited.add((next_x, next_y))
                queue.append((next_x, next_y))
              
        
    def is_valid(self, grid, x, y, visited):
        m = len(grid)
        n = len(grid[0])
        
        if not (0 <= x < m and 0 <= y < n):
            return False
        
        if (x, y) in visited:
            return False
        
        if grid[x][y] == "0":
            return False
        return True