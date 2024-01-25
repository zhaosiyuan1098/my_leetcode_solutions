#
# @lc app=leetcode.cn id=2859 lang=python3
# @lcpr version=30113
#
# [2859] 计算 K 置位下标对应元素的和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total_sum = 0
        for i, n in enumerate(nums):
            if bin(i).count('1') == k:
                total_sum += n
        return total_sum
# @lc code=end



#
# @lcpr case=start
# [5,10,1,5,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n2\n
# @lcpr case=end

#

