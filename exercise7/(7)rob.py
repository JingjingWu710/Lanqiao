class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #这道题需要不断地问偷还是不偷这个问题，且没有到最后一个节点，就不能得知之前的节点是偷还是不偷
        #所以要深度搜索，嵌套循环
        def dfs(root):
            if not root:
                return 0,0
            #这个循环会运行到最后一个节点
            l_steal, l_notsteal = dfs(root.left)
            r_steal, r_notsteal = dfs(root.right)
            #体现了偷和不偷两种情况，偷：原根节点加以左右子节点AB为根节点时不偷AB，原根节点的孙节点的最大值
            #不偷原根节点，把左右子节点算进去，求最大值
            return root.val+l_notsteal+r_notsteal, max(l_steal,l_notsteal)+max(r_steal,r_notsteal)
        return max(dfs(root)) 