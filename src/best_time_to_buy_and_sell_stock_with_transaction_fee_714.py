#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: ran
    @file: best_time_to_buy_and_sell_stock_with_transaction_fee_714.py
    @time: 2021/6/25 下午4:03
    @desc:
        买卖股票的最佳时机含手续费
        给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格；非负整数 fee 代表了交易股票的手续费用。
        你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
        返回获得利润的最大值。
        注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

        状态定义：dp[i][0, 1]为最大收益 0表示不持有股票 1表示持有股票
"""


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        profit = [[0, 0] for _ in range(n)]
        profit[0][1] = -prices[0]

        for i in range(1, n):
            profit[i][0] = max(profit[i - 1][0], profit[i - 1][1] + prices[i] - fee)
            profit[i][1] = max(profit[i - 1][1], profit[i - 1][0] - prices[i])

        return profit[n - 1][0]

    def maxProfit2(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0

        buy, sell = float('-inf'), 0
        for p in prices:
            buy = max(buy, sell - p)
            sell = max(sell, buy + p - fee)

        return sell
