# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,ans,root):
        if root is None:
            return
        
        self.solve(ans,root.left)
        self.solve(ans,root.right)
        ans.append(root.val)


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.solve(ans,root)
        return ans