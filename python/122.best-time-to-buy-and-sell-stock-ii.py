#
# @lc app=leetcode.cn id=122 lang=python3
# @lcpr version=30114
#
# [122] 买卖股票的最佳时机 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        all=0
        for i in range(1,len(prices)):
            c=prices[i]-prices[i-1]
            if c>0:
                all+=c
        return all
# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#

