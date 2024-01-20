# @lcpr-before-debug-begin
from python3problem2 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30113
#
# [2] 两数相加
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # 创建一个虚拟头节点
        curr = dummy  # 当前节点指针
        carry = 0  # 进位值
        
        while l1 or l2 or carry:
            # 计算当前位的和
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            # 更新进位值和当前节点的值
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end
