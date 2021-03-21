# 给定一个二叉树，在树的 最后一行 找到 最左边 的值;
# 注意: 您可以假设树（即给定的根节点）不为 NULL
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findBottomLeftValue(self, root: TreeNode) -> int:
        # BFS Advanced
        queue = [root]
        while(queue):
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node

    def findBottomLeftValue3(self, root: TreeNode) -> int:
        # BFS
        last_left = root
        queue = [root]
        while(queue):
            lvl = queue[:]
            queue.clear()
            last_left = lvl[0]
            while(lvl):
                node = lvl.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return last_left.val

    def findBottomLeftValue(self, root: TreeNode) -> int:
        # depth, value when MAX;
        max_n = [0, root.val]

        def dfs(root: TreeNode, depth: int) -> int:
            if not root:
                return
            if not root.left and not root.right and depth > max_n[0]:
                # 1st LEFT leaf in deepest level
                max_n[0] = depth
                max_n[1] = root.val
            depth += 1
            dfs(root.left, depth)
            dfs(root.right, depth)

        dfs(root, 1)
        return max_n[1]
