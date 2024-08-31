class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(tree=root):
            if not tree:
                return

            dfs(tree.left)
            dfs(tree.right)

            tmp = min(tree.left.val if tree.left else float("inf"), tree.right.val if tree.right else float("inf"))

            if tmp == 0:
                res[0] += 1
                tree.val = 1
            if tmp == 1:
                tree.val = 2

        dfs()
        return (root.val == 0) + res[0]
            
