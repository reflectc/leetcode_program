#! usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: ran
    @file: best_time_to_buy_and_sell_stock_with_cooldown_309.py
    @time: 2021/6/25 下午2:44
    @desc:
        最佳买卖股票时机含冷冻期
        给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
        设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
        你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
        卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
        示例:
        输入: [1,2,3,0,2]
        输出: 3
        解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

        状态定义：
        dp[i][0] dp[i][1] dp[i][2] 分别代表第i天 持有股票最大收益 不持有股票且处于冷冻期 不持有股票且不处于冷冻期
        这里的 处于冷冻期 指的是在第 i 天结束之后的状态。
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        profit = [[0 for _ in range(3)] for _ in range(n)]
        profit[0][0] = -prices[0]

        for i in range(1, n):
            profit[i][0] = max(profit[i - 1][0], profit[i - 1][2] - prices[i])
            profit[i][1] = profit[i - 1][0] + prices[i]
            profit[i][2] = max(profit[i - 1][2], profit[i - 1][1])

        return max(profit[n - 1][1], profit[n - 1][2])

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        buy, pre_sell, sell = float('-inf'), 0, 0
        for p in prices:
            buy = max(buy, pre_sell - p)
            pre_sell = sell
            sell = max(sell, buy + p)

        return sell
