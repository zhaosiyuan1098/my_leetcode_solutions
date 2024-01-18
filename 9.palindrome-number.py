#
# @lc app=leetcode.cn id=9 lang=python3
# @lcpr version=30113
#
# [9] 回文数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        old_j=0
        absx=abs(x)
        # #获取x的位数
        # for i in range(31):
        #     if x // 10**i == 0:
        #         break
        # for j in range(i):
        #     if x // 10**j % 10 != x // 10**(i-j-1) % 10:
        #         return False
        # else:
        #     return True
        while (absx>0):
            #j为x除10的余数
            j = absx % 10
            absx = absx // 10
            old_j = old_j * 10 + j
        return old_j == abs(x)
# @lc code=end



#
# @lcpr case=start
# 121\n
# @lcpr case=end

# @lcpr case=start
# -121\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#

def main():
    sol=Solution()
    sol.isPalindrome(432)
    
main()