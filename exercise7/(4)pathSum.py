class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
from typing import Optional

def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    ans = []
    def dfs(node,targetSum,path):
        if not node:
            return
        #记录路径
        path.append(node.val)
        targetSum -= node.val
        if targetSum == 0 and not node.left and not node.right:
            ans.append(list(path))
        #探索当前节点的子节点
        dfs(node.left,targetSum,path)
        dfs(node.right,targetSum,path)
        #探索完一条路径就删掉它
        path.pop()
    dfs(root,targetSum,[])
    return ans

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

targetSum = int(input())
print(pathSum(root,targetSum))