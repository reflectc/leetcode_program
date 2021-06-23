#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: ran
    @file: best_time_to_buy_and_sell_stock_II_122.py
    @time: 2021/6/22 下午9:27
    @desc:
        买卖股票的最佳时机 II
        给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

        定义状态：DP二维数组DP[i][0, 1]表示最大利润 第一维度为到第i天 第二维度0，1表示此时是否持有股票
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
        profit = [[0 for _ in range(2)] for _ in range(len(prices))]
        profit[0][0], profit[0][1] = 0, -prices[0]

        for i in range(1, len(prices)):
            profit[i][0] = max(profit[i - 1][0], profit[i - 1][1] + prices[i])
            profit[i][1] = max(profit[i - 1][1], profit[i - 1][0] - prices[i])
            res = max(res, profit[i][0], profit[i][1])

        return res
