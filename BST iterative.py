class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        cur = self.root
        while True:
            if new_val > cur.value:
                if cur.right is None:
                    cur.right = Node(new_val)
                    break
                else:
                    cur = cur.right
            else:
                if cur.left is None:
                    cur.left = Node(new_val)
                    break
                else:
                    cur = cur.left

    def search(self, find_val):
        cur = self.root
        while True:
            if find_val == cur.value:
                return True
            elif find_val > cur.value:
                if cur.right is None:
                        return False
                else:
                    cur = cur.right
            else:
                if cur.left is None:
                        return False
                else:
                    cur = cur.left
        
    
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
#t = []
#tree.preorder_print(tree.root,t)
#print(t)
# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))