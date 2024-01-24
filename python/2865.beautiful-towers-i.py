# @lcpr-before-debug-begin
from python3problem2865 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=2865 lang=python3
# @lcpr version=30113
#
# [2865] 美丽塔 I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        max=0
        for i in range(len(maxHeights)):
            peak=maxHeights[i]
            high=peak
            total=0
            for j in range(i,len(maxHeights)):
                if high>maxHeights[j]:
                    high=maxHeights[j]
                total+=high
            high=peak
            for k in range(i-1,-1,-1):
                if high>maxHeights[k]:
                    high=maxHeights[k]
                total+=high
            if total>max:
                max=total
        return max
# @lc code=end


# @lcpr-div-debug-arg-start
# funName=maximumSumOfHeights
# paramTypes= ["number[]"]
# @lcpr-div-debug-arg-end




#
# @lcpr case=start
# [5,3,4,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [6,5,3,9,2,7]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,5,5,2,3]\n
# @lcpr case=end

#

