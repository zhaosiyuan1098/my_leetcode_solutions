# @lcpr-before-debug-begin
from python3problem486 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=486 lang=python3
# @lcpr version=30113
#
# [486] 预测赢家
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if not len(nums)%2:
            return True
        maxdiff=[[0]*len(nums) for i in range(len(nums))]
        for i in range(len(nums)):
            maxdiff[i][i]=nums[i]
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1,len(nums)):
                maxdiff[i][j]=max(nums[i]-maxdiff[i+1][j],nums[j]-maxdiff[i][j-1])
        return maxdiff[0][-1]>=0
# @lc code=end



#
# @lcpr case=start
# [1,5,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,5,233,7]\n
# @lcpr case=end

#

