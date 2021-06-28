#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: ran
    @file: longest_increasing_subsequence_300.py
    @time: 2021/6/28 18:56
    @desc:
        最长递增子序列
        给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
        子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
        例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
        示例 1：
        输入：nums = [10,9,2,5,3,7,101,18]
        输出：4
        解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        贪心 + 二分
        """
        if not nums:
            return 0

        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                ins_loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        ins_loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[ins_loc] = n
        return len(d)
