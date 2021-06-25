#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: ran
    @file: best_time_to_buy_and_sell_stock_IV_188.py
    @time: 2021/6/23 下午2:41
    @desc:
        买卖股票的最佳时机 IV
        给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [[0 for _ in range(k + 1)] for _ in range(n)]
        sell = [[0 for _ in range(k + 1)] for _ in range(n)]
        buy[0][0] = -prices[0]

        for i in range(1, k + 1):
            buy[0][i] = sell[0][i] = float('-inf')

        for i in range(1, n):
            buy[i][0] = max(buy[i - 1][0], sell[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j - 1] + prices[i])

        return max(sell[n - 1])

    def maxProfit2(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)

        for p in prices:
            for kk in range(1, k + 1):
                buy[kk] = max(buy[kk], sell[kk - 1] - p)
                sell[kk] = max(sell[kk], buy[kk] + p)
        return sell[k]
