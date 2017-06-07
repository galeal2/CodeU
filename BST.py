from node import Node
class BST:
    def __init__(self, lst = None):
        self.root = None
        if lst != None:
            for key in lst:
                self.add(key)

    def add(self, key):
        if self.root == None:
            self.root = Node(key, None, None)
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if key < child_tree.key: 
                    child_tree = child_tree.left 
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if key < parent.key:
                parent.left = Node(key, None, None)
            else:
                parent.right = Node(key, None, None)
