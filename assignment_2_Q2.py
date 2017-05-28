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
        return [BT.root.item]
    if not rec_find_ancestors(ptr, key, []):
        return []
    return rec_find_ancestors(ptr, key, [])


# find the lowest common ancestor
def find_common_ancestor(BT, node1, node2):
    n1_ancestors = set(find_ancestors(BT, node1)+[node1])
    n2_ancestors = set(find_ancestors(BT, node2)+[node2])
    if not n1_ancestors.intersection(n2_ancestors):
        return []
    return list(n1_ancestors.intersection(n2_ancestors))[-1]

# tests
def main():
    tree = BST([16, 9, 18, 3, 14, 19, 1, 5])
    assert find_common_ancestor(tree, 3, 14) == 9
    assert find_common_ancestor(tree, 3, 0) == []
    assert find_common_ancestor(tree, 9, 19) == 16
    assert find_common_ancestor(tree, 10, 30) == []
    assert find_common_ancestor(tree, 16, 1) == 16
    assert find_common_ancestor(tree, 3, 1)  == 3
if __name__ == "__main__":
    main()
