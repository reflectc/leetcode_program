#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    @author: ran
    @file: triangle_120.py
    @time: 2021/6/20 16:25
    @desc:
        三角形最小路径和
        给定一个三角形 triangle ，找出自顶向下的最小路径和。
        每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层
        结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行
        的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

        动态规划解题 思路：
        1.定义状态
            DP[i, j] 为从最下面节点到[i, j]节点走的路径和的最小值
        2.DP方程：列出状态转移方程
            DP[i, j] = min(DP[i+1, j], DP[i+1, j+1]) + triangle[i, j]
        核心思想：反向进行递推
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        res = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = triangle[i][j] + min(res[j], res[j + 1])

        return res[0]
