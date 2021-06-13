#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    @author: ran
    @file: number_of_1_bits_191.py
    @time: 2021/6/13 18:12
    @desc:
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        flag = 1

        # solution 1 --
        # while n != 0:
        #     res += 1
        #     n &= n -1
        # return res

        # solution 2 --
        for i in range(32):
            if n & flag:
                res += 1
            flag = flag << 1
        return res
