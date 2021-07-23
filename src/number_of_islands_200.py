#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: ran
    @file: number_of_islands_200.py
    @time: 2021/7/22 16:15
    @desc:
        岛屿数量
        给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
        岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
        此外，你可以假设该网格的四条边均被水包围。
        示例 1：
        输入：grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        输出：1

        解题：1.并查集  2.DFS
"""


class UnionFind(object):
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class Solution1(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        uf = UnionFind(grid)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                for d in directions:
                    dx, dy = i + d[0], j + d[1]
                    if dx >= 0 and dy >= 0 and dx < m and dy < n and grid[dx][dy] == '1':
                        uf.union(i * n + j, dx * n + dy)

        return uf.count


class Solution2(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        self.max_x = len(grid)
        self.max_y = len(grid[0])
        self.grid = grid
        self.visited = set()
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        return sum([self.floodfill_DFS(i, j) for i in range(self.max_x) for j in range(self.max_y)])

    def floodfill_DFS(self, x, y):
        if not self._is_valid(x, y):
            return 0
        self.visited.add((x, y))
        for k in range(4):
            self.floodfill_DFS(x + self.dx[k], y + self.dy[k])
        return 1

    def _is_valid(self, x, y):
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y:
            return False
        if self.grid[x][y] == '0' or ((x, y) in self.visited):
            return False
        return True
