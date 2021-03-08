
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        lonely_nodes = []
        self.exploreLonelyNodes(root, lonely_nodes)
        return lonely_nodes

    def exploreLonelyNodes(self, root, lonely_nodes):
        if root and root.left is not None and root.right is None:
            lonely_nodes.append(root.left.val)
            self.exploreLonelyNodes(root.left, lonely_nodes)
        elif root and root.right is not None and root.left is None:
            lonely_nodes.append(root.right.val)
            self.exploreLonelyNodes(root.right, lonely_nodes)
        elif root.left is None and root.right is None:
            return
        else:
            self.exploreLonelyNodes(root.left, lonely_nodes)
            self.exploreLonelyNodes(root.right, lonely_nodes)


#solution using stack

class Solution2:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        lonely_nodes = []
        self.exploreLonelyNodes(root, lonely_nodes)
        return lonely_nodes

    def exploreLonelyNodes(self, root, lonely_nodes):
        if root and root.left is not None and root.right is None:
            lonely_nodes.append(root.left.val)
            self.exploreLonelyNodes(root.left, lonely_nodes)
        elif root and root.right is not None and root.left is None:
            lonely_nodes.append(root.right.val)
            self.exploreLonelyNodes(root.right, lonely_nodes)
        elif root.left is None and root.right is None:
            return
        else:
            self.exploreLonelyNodes(root.left, lonely_nodes)
            self.exploreLonelyNodes(root.right, lonely_nodes)
