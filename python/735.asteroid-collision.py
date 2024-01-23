# @lcpr-before-debug-begin
from python3problem735 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=735 lang=python3
# @lcpr version=30113
#
# [735] 小行星碰撞
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        

        
        
        asteroids.append(0)
        for i in range(len(asteroids)):
            if asteroids[i]<=0:
                continue
            else:
                if i==len(asteroids)-1:
                    break
                j=i
                for j in range(i,len(asteroids)):
                    if asteroids[j]>0:
                        continue
                    else:
                        break
                for k in range(j,len(asteroids)):
                    if asteroids[k]<0:
                        continue
                    else:
                        break
                for n in range(len(asteroids)):
                    if asteroids[n]<=0:
                        continue
                    else:
                        break
                w=j-1
                m=j
                while w>=n and m<=k-1 and j<=len(asteroids)-1 and k<=len(asteroids)-1:
                    
                    if abs(asteroids[w])>abs(asteroids[m]):
                        asteroids[m]=0
                        m=m+1
                        if m>k:
                            break 
                    elif abs(asteroids[w])<abs(asteroids[m]):
                        asteroids[w]=0
                        w=w-1
                        if w<n:
                            break 
                    else:
                        asteroids[w]=0
                        asteroids[m]=0
                        w=w-1
                        m=m+1
        while 0 in asteroids:
            asteroids.remove(0)
        return asteroids

                        
                        
                
        # max=0
        # inv_max_num=0
        # for i in range(len(asteroids)):
        #     if max<abs(asteroids[i]):
        #         max=asteroids[i]
        # for i in range(len(asteroids)):
        #     if asteroids[i]==-max:
        #         inv_max_num=inv_max_num+1
        # print (inv_max_num)
        # print (max)
        # if inv_max_num:
        #     return []
        # else :
        #     for i in range(len(asteroids)-1):
        #         if asteroids[i]*max>0 and asteroids[i+1]*max<0:
        #             if abs(asteroids[i])>abs(asteroids[i+1]):
        #                 asteroids[i+1]=0
        #             elif abs(asteroids[i])<abs(asteroids[i+1]):
        #                 asteroids[i]=0
        #             else:
        #                 asteroids[i]=0
        #                 asteroids[i+1]=0
        #     for i in range(len(asteroids)):
        #         if asteroids[i]*max<0:
        #             asteroids[i]=0
        #     #除去asteroilds中的0
        #     while 0 in asteroids:
        #         asteroids.remove(0)
                    
        #     print(asteroids)
        #     return asteroids

            
# @lc code=end



#
# @lcpr case=start
# [5,10,-5]\n
# @lcpr case=end

# @lcpr case=start
# [8,-8]\n
# @lcpr case=end

# @lcpr case=start
# [10,2,-5]\n
# @lcpr case=end

#

