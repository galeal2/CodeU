class Node:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self, lst = None):
        self.root = None
        if lst != None:
            for item in lst:
                self.add(item)

    def add(self, item):
        if self.root == None:
            self.root = Node(item, None, None)
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: 
                    child_tree = child_tree.left 
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)



# find all ancestors for a Binary Tree
def rec_find_ancestors(ptr, key, path):
    if ptr == None:
        return False
    if ptr.item == key:
        return True
    if rec_find_ancestors(ptr.left, key, path) or rec_find_ancestors(ptr.right, key, path):
        path += [ptr.item]
        return path
    return False

def find_ancestors(BT, key):
    ptr = BT.root
    if BT.root.item == key:
        return None
    if not rec_find_ancestors(ptr, key, []):
        return None
    return rec_find_ancestors(ptr, key, [])

# tests
def main():
    
    tree = BST([16, 9, 18, 3, 14, 19, 1, 5]) 
    assert (find_ancestors(tree, 5)) == [3, 9, 16]
    assert (find_ancestors(tree, 14)) == [9, 16]
    assert (find_ancestors(tree, 16)) == None
    assert (find_ancestors(tree, 18)) == [16]
    assert (find_ancestors(tree, 19)) == [18, 16]
    assert (find_ancestors(tree, 20)) == None
    assert(find_ancestors(tree, '.')) == None

    tree2 = BST(['F','D', 'I', 'B', 'E', 'L', 'A'])
    assert(find_ancestors(tree2, 'B')) == ['D', 'F']
    assert(find_ancestors(tree2, 3)) == None
    
if __name__ == "__main__":
    main()
