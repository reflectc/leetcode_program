#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    @author: ran
    @file: power_of_two_231.py
    @time: 2021/6/13 19:42
    @desc:
        2 的幂
        给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
        如果存在一个整数 x 使得 n == 2ˣ ，则认为 n 是 2 的幂次方。
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 2的幂 n的二进制只有1个1 所以要判断 n & n-1 是否为0
        return n > 0 and not (n & n - 1)
