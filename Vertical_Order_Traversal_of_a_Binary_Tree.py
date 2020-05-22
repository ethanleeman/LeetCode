# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversalHelper(self, r,dic,x,y):
        if ((y,x) in dic.keys()):
            L = dic[(y,x)]
            L.append(r.val)
            dic[(y,x)] = L
        else:
            dic[(y,x)] = [r.val]
        if (r.left != None):
            self.verticalTraversalHelper(r.left,dic,x-1,y+1)
        if (r.right != None):
            self.verticalTraversalHelper(r.right,dic,x+1,y+1)
        return dic


    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = {}
        self.verticalTraversalHelper(r = root,dic = d ,x=0,y=0)

        cp = d.keys()[:]
        cp.sort()
        L = []
        min_x = 0
        max_x = 0

        for k in cp:
            if (k[1] < min_x):
                min_x = k[1]
            if (k[1] > max_x):
                max_x = k[1]

        for i in range(min_x, max_x + 1):
            add = []
            for k in cp:
                if (k[1] == i):
                    add2 = (d[k])[:]
                    add2.sort()
                    for j in add2:
                        add.append(j)
            L.append(add)
        return L
