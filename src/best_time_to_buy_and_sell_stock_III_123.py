#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: ran
    @file: best_time_to_buy_and_sell_stock_III_123.py
    @time: 2021/6/23 上午10:38
    @desc:
        买卖股票的最佳时机 III
        给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
        设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

        这里 买入+卖出 为 交易一次
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        profit = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]
        profit[0][0][0], profit[0][0][1] = 0, -prices[0]
        profit[0][1][0], profit[0][1][1] = float('-inf'), float('-inf')
        profit[0][2][0], profit[0][2][1] = float('-inf'), float('-inf')

        n = len(prices)
        for i in range(1, n):
            profit[i][0][0] = profit[i - 1][0][0]
            profit[i][0][1] = max(profit[i - 1][0][1], profit[i - 1][0][0] - prices[i])

            profit[i][1][0] = max(profit[i - 1][1][0], profit[i - 1][0][1] + prices[i])
            profit[i][1][1] = max(profit[i - 1][1][1], profit[i - 1][1][0] - prices[i])

            profit[i][2][0] = max(profit[i - 1][2][0], profit[i - 1][1][1] + prices[i])

        return max(profit[n - 1][0][0], profit[n - 1][1][0], profit[n - 1][2][0])

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy1, sell1 = -prices[0], 0
        buy2, sell2 = -prices[0], 0

        for i in range(1, len(prices)):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2
