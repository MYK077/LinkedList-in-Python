# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants
# (where we allow a node to be a descendant of itself).”

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

class LowersCommonAncestor:
    def lowersCommonAncestor(self, root, p, q):
        if not root:
            return None
        left_res = self.lowersCommonAncestor(root.left, p, q)
        right_res = self.lowersCommonAncestor(root.right, p, q)

        if (left_res and right_res) or root in ([p, q]):
            return root
        else:
            return left_res or right_res
