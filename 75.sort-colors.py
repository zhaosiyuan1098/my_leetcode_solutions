# @lcpr-before-debug-begin
from python3problem75 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30113
#
# [75] 颜色分类
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        small_num=0
        big_num=0
        for i in range(len(nums)):
            if nums[i]==0:
                small_num=small_num+1
            if nums[i]==2:
                big_num=big_num+1
        
        
        for j in range(small_num):
            nums[j]=0
        for w in range(small_num,len(nums)-big_num):
            nums[w]=1
        for k in range(big_num):
            nums[len(nums)-k-1]=2
            
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#

