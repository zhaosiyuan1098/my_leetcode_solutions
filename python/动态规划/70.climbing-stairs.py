# @lcpr-before-debug-begin
from python3problem70 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=30114
#
# [70] 爬楼梯
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        max=[0]*(n+1)
        max[0],max[1]=1,1
        for i in range(2,n+1):
            # print(i)
            max[i]=max[i-1]+max[i-2]
        return max[-1]
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

