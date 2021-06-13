#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    @author: ran
    @file: power_of_two_231.py
    @time: 2021/6/13 19:42
    @desc:
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 2的幂 n的二进制只有1个1 所以要判断 n & n-1 是否为0
        return n > 0 and not (n & n - 1)
