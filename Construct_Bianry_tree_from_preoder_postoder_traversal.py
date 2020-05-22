# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])

        #print(pre)
        #print(post)
        root = TreeNode(pre[0])
        pre = pre[1:]
        post = post[:-1]


        if pre[0] == post[-1]:
            root.left = self.constructFromPrePost(pre,post)
        else:
            pre_index = pre.index(post[-1])
            post_index = post.index(pre[0])
            leftpre = pre[:pre_index]
            leftpost = post[:post_index+1]
            rightpre = pre[pre_index:]
            rightpost = post[post_index:]
            root.left = self.constructFromPrePost(leftpre,leftpost)
            root.right = self.constructFromPrePost(rightpre,rightpost)
        return root
