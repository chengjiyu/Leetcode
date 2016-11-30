class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # calcuate number of 1 and *4
        l = 0
        for i in grid:
            l += sum(i)
        p = 4*l

        # calcuate the repeat side, if 1 is adjacent and minus 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i+1 < len(grid) and grid[i][j] == grid[i+1][j] == 1:
                    p -= 2
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if j+1 < len(grid[0]) and grid[i][j] == grid[i][j+1] == 1:
                    p -= 2
        return p