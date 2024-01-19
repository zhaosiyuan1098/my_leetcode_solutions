#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30113
#
# [48] 旋转图像
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        matrix2 = [row[:] for row in matrix]  # 创建matrix2的副本
        
        for i in range(n):
            for j in range(n):
                matrix[j][n-1-i] = matrix2[i][j]  # 修正索引范围
        
        """
        Do not return anything, modify matrix in-place instead.
        """
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#

#一开始我也想到了想题解那样的直接交换四个值，但是卡在如何选定小方块的大小了，看了题解后才发现大小是  [n//2+n%2,n//2],
#另外，题解中给出了很好的O（n）复杂度的遍历[n//2+n%2,n//2]方法。