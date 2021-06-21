#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: ran
    @file: maximum_product_subarray_152.py
    @time: 2021/6/21 下午7:12
    @desc:
        乘积最大子数组
        给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
        示例：
        输入: [2,3,-2,4]
        输出: 6
        解释: 子数组 [2,3] 有最大乘积 6。
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        res, cur_max, cur_min = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            cur_max, cur_min = cur_max * num, cur_min * num
            cur_max, cur_min = max(cur_max, cur_min, num), min(cur_max, cur_min, num)
            res = cur_max if cur_max > res else res

        return res

    def maxProduct2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0

        dp = [[0 for _ in range(2)] for _ in range(2)]
        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            # 滚动数组
            x, y = i % 2, (i - 1) % 2
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max(res, dp[x][0])

        return res
