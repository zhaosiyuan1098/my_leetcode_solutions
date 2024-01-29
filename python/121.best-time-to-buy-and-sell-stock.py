# @lcpr-before-debug-begin
from python3problem121 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30114
#
# [121] 买卖股票的最佳时机
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit
        # maxdiff=[[None]*len(prices) for i in range(len(prices))]
        # for i in range(len(prices)):
        #     maxdiff[i][i]=0
        # for diff in range(1,len(prices)):
        #     for j in range(len(prices)-diff):
        #         maxdiff[j][j+diff]=max(maxdiff[j+1][j+diff],maxdiff[j][j+diff-1],prices[j+diff]-prices[j])
        # # print(maxdiff)
        # return maxdiff[0][-1]      
# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#

