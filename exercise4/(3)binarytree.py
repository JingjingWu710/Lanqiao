class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
from typing import Optional

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    result = []
    q = []
    # 如果root是空集：
    if not root:
        return []
    # 把root加入队列，这样之后可以一层层遍历
    q.append(root)
    while q:
        current_level = []
        # 先遍历第一层
        for i in q:
            current_level.append(i.val)
        result.append(current_level)
        # 新列表存放下一层
        tmp = []
        for i in q:
            # 把下一层节点都加入临时列表
            if i.left:
                tmp.append(i.left)
            if i.right:
                tmp.append(i.right)
        # 让队列等于临时列表，下一个循环把它扫入最终列表
        q = tmp
    return result

# 创建二叉树
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# 使用创建好的二叉树调用 levelOrder 函数
print(levelOrder(root))


    # if len(root) == 0:
    #     return []
    # elif len(root) == 1:
    #     return [root]
    # else:
    #     result = []
    #     for i in range(len(root)[::2]):
    #         if i == 0:
    #             result.append([i])
    #         else: