# @lcpr-before-debug-begin
from python3problem45 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30113
#
# [45] 跳跃游戏 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def tonext():
        
        pass

    def jump(self, nums: List[int]) -> int:
        # 创建一个和nums长度相同，值全为none的数组
        minjumparray = [None] * len(nums)
        minjumparray[0]=0
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            if minjumparray[i] is not None:
                for j in range(i+1,nums[i]+i+1):
                    if j<len(nums):
                        if minjumparray[j] is None or minjumparray[j]>minjumparray[i]+1:
                            minjumparray[j]=minjumparray[i]+1
                # print(minjumparray)
        if minjumparray[-1] is None:
            return False
        else: 
            return minjumparray[-1]
                
        
        
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#


