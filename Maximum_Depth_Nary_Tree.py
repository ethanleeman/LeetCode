"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0

        biggest_depth = 0
        for child in root.children:
            current_depth = self.maxDepth(child)
            if current_depth > biggest_depth:
                biggest_depth = current_depth
        return biggest_depth + 1
