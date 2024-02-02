#
# @lc app=leetcode.cn id=1137 lang=python3
# @lcpr version=30114
#
# [1137] 第 N 个泰波那契数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        if n<3:
            t=[0,0,1]
            return t[n]
        else:
            t= [None]*(n+1)
            t[0],t[1],t[2]=0,1,1
        for i in range(3,n+1):
            t[i]=t[i-3]+t[i-2]+t[i-1]
        return t[-1]
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 25\n
# @lcpr case=end

#

