#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: ran
    @file: best_time_to_buy_and_sell_stock_121.py
    @time: 2021/6/22 下午3:58
    @desc:
        买卖股票的最佳时机
        给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
        你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
        返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

        这里股票只交易一次
        定义状态：
        DP二维数组DP[i][0, 1, 2]表示最大利润 第一维度为到第i天 第二维度0表示未买股票 1表示买入 2表示卖出
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        res = 0
        profit = [[0 for _ in range(3)] for _ in range(len(prices))]
        profit[0][0], profit[0][1], profit[0][2] = 0, -prices[0], 0

        for i in range(1, len(prices)):
            profit[i][0] = profit[i - 1][0]
            profit[i][1] = max(profit[i - 1][1], profit[i - 1][0] - prices[i])
            profit[i][2] = profit[i - 1][1] + prices[i]
            res = max(res, profit[i][0], profit[i][1], profit[i][2])

        return res

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        buy, sell = float('-inf'), 0
        for p in prices:
            buy = max(buy, -p)
            sell = max(sell, buy + p)

        return sell
