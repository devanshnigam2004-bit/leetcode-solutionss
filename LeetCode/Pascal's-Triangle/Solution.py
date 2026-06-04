1class Solution:
2    def generate(self, numRows: int) -> list[list[int]]:
3        triangle = [[1]]
4
5        for i in range(1, numRows):
6            row = [1]
7            for j in range(1, i):
8                row.append(triangle[i-1][j-1] + triangle[i-1][j])
9            row.append(1)
10            triangle.append(row)
11
12        return triangle