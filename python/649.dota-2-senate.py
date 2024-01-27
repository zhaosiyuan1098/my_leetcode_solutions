# @lcpr-before-debug-begin
from python3problem649 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=649 lang=python3
# @lcpr version=30113
#
# [649] Dota2 参议院
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senateflag = [1] * len(senate)
        
        while senate:
            
            for i in range(len(senate)):
                flag = 1
                if senateflag[i]==0:
                    continue
                else:
                    if senate[i]=='R':
                        for j in range(i+1,i+len(senate)):
                            if senate[j%len(senate)]=='D' and senateflag[j%len(senate)]==1:
                                senateflag[j%len(senate)]=0
                                flag = 0
                                break
                        if flag:
                            return 'Radiant'
                    if senate[i]=='D':
                        for j in range(i+1,i+len(senate)):
                            if senate[j%len(senate)]=='R' and senateflag[j%len(senate)]==1:
                                senateflag[j%len(senate)]=0
                                flag = 0
                                break
                        if flag:
                            return 'Dire'
  
# @lc code=end



#
# @lcpr case=start
# "RD"\n
# @lcpr case=end

# @lcpr case=start
# "RDD"\n
# @lcpr case=end

#

