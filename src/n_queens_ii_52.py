#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    @author: ran
    @file: n_queens_ii_52.py
    @time: 2021/6/14 1:23
    @desc:
"""


# n皇后问题 研究的是如何将 n个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数n，返回 n皇后问题 不同的解决方案的数量。
# 这里用位操作求解

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return []
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count

    def DFS(self, n, row, cols, pie, na):
        if row >= n:
            self.count += 1
            return

        # 得到当前所有的空位
        bits = (~(cols | pie | na)) & ((1 << n) - 1)

        while bits:
            # 取到最低位的1
            p = bits & -bits
            self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
            # 去掉最低位的1
            bits = bits & (bits - 1)
