1class Solution:
2    def countNegatives(self, grid: list[list[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4        row, col = 0, n - 1
5        count = 0
6
7        while row < m and col >= 0:
8            if grid[row][col] < 0:
9                count += m - row
10                col -= 1
11            else:
12                row += 1
13
14        return count
15
16
17
18        