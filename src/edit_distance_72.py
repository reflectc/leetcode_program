#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: ran
    @file: edit_distance_72.py
    @time: 2021/7/13 20:55
    @desc:
        编辑距离
        给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
        你可以对一个单词进行如下三种操作：
        插入一个字符
        删除一个字符
        替换一个字符

        示例 1：
        输入：word1 = "horse", word2 = "ros"
        输出：3
        解释：
        horse -> rorse (将 'h' 替换为 'r')
        rorse -> rose (删除 'r')
        rose -> ros (删除 'e')

        定义状态：DP二维数组DP[i][j] 表示word1前i个字符转换成word2前j个字符所用最少操作数
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        if m * n == 0:
            return m + n

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1),
                               dp[i - 1][j] + 1,
                               dp[i][j - 1] + 1)

        return dp[m][n]
