"""
Program to find lease common ancestor for the two given nodes in a binary tree
"""
class TreeNode: 
  
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
  
def findLCAUtil(root, n1, n2, v): 
    if root is None: 
        return None
  
    if root.key == n1 : 
        v[0] = True
        return root 
  
    if root.key == n2: 
        v[1] = True
        return root 
  
    left_lca = findLCAUtil(root.left, n1, n2, v) 
    right_lca = findLCAUtil(root.right, n1, n2, v) 
  
    if left_lca and right_lca: 
        return root  
    return left_lca if left_lca is not None else right_lca 
  
  
def find(root, k): 
    if root is None: 
        return False
      
    if (root.key == k or find(root.left, k) or
        find(root.right, k)): 
        return True
    return False
  
def findLCA(root, n1, n2): 
    v = [False, False] 
    lca = findLCAUtil(root, n1, n2, v) 
  
    if (v[0] and v[1] or v[0] and find(lca, n2) or v[1] and 
        find(lca, n1)): 
        return lca 
    return None
  
 
root = TreeNode(2) 
root.left = TreeNode(1) 
root.right = TreeNode(3) 
root.right.left = TreeNode(4) 
root.right.right = TreeNode(5) 
root.right.right.left = TreeNode(6) 
  
lca = findLCA(root, 1, 5) 
if lca is not None: 
    print ("LCA(1, 5) = ", lca.key )
else : 
    print ("Keys are not present")
