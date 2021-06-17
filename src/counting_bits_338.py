#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    @author: ran
    @file: counting_bits_338.py
    @time: 2021/6/13 19:52
    @desc:
        给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，
        计算其二进制数中的 1 的数目并将它们作为数组返回。
"""


class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i & (i - 1)] + 1
        return res
