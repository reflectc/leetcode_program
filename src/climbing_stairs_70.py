#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: ran
    @time: 2021/6/17 下午8:37
    @file: climbing_stairs_70.py
    @desc:
        爬楼梯
        假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
        每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
        注意：给定 n 是一个正整数。
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        s1, s2 = 1, 2
        for _ in range(2, n):
            s1, s2 = s2, s1 + s2
        return s2
