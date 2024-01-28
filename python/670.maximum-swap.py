# @lcpr-before-debug-begin
from python3problem670 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=670 lang=python3
# @lcpr version=30114
#
# [670] 最大交换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        #获取num的位数
        num_len=len(str(num))
        
        new=[]
        max_indx=0
        for i in range(num_len):
            cur=num//10**(num_len-1-i)%10
            new.append(cur)
            # print(new)
            
        #对new进行排序
        sort_new=sorted(new,reverse=True)
        
        for i in range(num_len):
            if new[i]==sort_new[i]:
                continue
            else:
                old_new_i=new[i]
                new[i]=sort_new[i]
                for j in range(i+1,num_len):
                    if new[j]==sort_new[i]:
                        flag=j
                new[flag]=old_new_i        
                num=0
                for w in range(num_len):
                    num+=new[w]*10**(num_len-1-w)
                return num
        return num
        
            
# @lc code=end



#
# @lcpr case=start
# 2736\n
# @lcpr case=end

# @lcpr case=start
# 9973\n
# @lcpr case=end

#

