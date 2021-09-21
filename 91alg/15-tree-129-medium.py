# 129. 求根到叶子节点数字之和
# 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
# 每条从根节点到叶节点的路径都代表一个数字：计算从根节点到叶节点生成的 所有数字之和 。
# - 示例 2：
#     输入：root = [4,9,0,5,1]
#     输出：1026
# - 解释：
#     从根到叶子节点路径 4->9->5 代表数字 495
#     从根到叶子节点路径 4->9->1 代表数字 491
#     从根到叶子节点路径 4->0 代表数字 40
#     因此，数字总和 = 495 + 491 + 40 = 1026
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # BFS
        if not root:
            return 0
        sum = 0
        queue, num_queue = [root], [root.val]
        while(queue):
            lvl = queue[:]
            queue.clear()
            while(lvl):
                node = lvl.pop(0)
                # do sth
                num = num_queue.pop(0)
                if not node.left and not node.right:
                    sum += num
                if node.left:
                    queue.append(node.left)
                    num_queue.append(num * 10 + node.left.val)
                if node.right:
                    queue.append(node.right)
                    num_queue.append(num * 10 + node.right.val)
        return sum

    def sumNumbers2(self, root: TreeNode) -> int:
        # DFS
        def dfs(root: TreeNode, sum: int) -> int:
            if not root:
                return 0
            sum = sum * 10 + root.val
            if not root.left and not root.right:
                # leaf
                return sum
            return dfs(root.left, sum) + dfs(root.right, sum)

        return dfs(root, 0)
