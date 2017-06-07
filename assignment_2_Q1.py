from BST import BST

# find all ancestors for a Binary Tree
def recursive_find_ancestors(ptr, key, ancestors):
    """ the function takes the root of a BST and a key
         and returns the ancestors of that key """
    if ptr == None:
        return False
    if ptr.key == key:
        return True
    if recursive_find_ancestors(ptr.left, key, ancestors) or recursive_find_ancestors(ptr.right, key, ancestors):
        ancestors += [ptr.key]
        return ancestors
    return False

def find_ancestors(BT, key):
    ptr = BT.root
    if ptr.key == key:
        return []
    if not recursive_find_ancestors(ptr, key, []):
        return []
    return recursive_find_ancestors(ptr, key, [])

# tests
def main():
    tree = BST([16, 9, 18, 3, 14, 19, 1, 5]) 
    assert (find_ancestors(tree, 5)) == [3, 9, 16]
    assert (find_ancestors(tree, 14)) == [9, 16]
    assert (find_ancestors(tree, 16)) == []
    assert (find_ancestors(tree, 18)) == [16]
    assert (find_ancestors(tree, 19)) == [18, 16]
    assert (find_ancestors(tree, 20)) == []
    assert(find_ancestors(tree, '.')) == []

    tree2 = BST(['F','D', 'I', 'B', 'E', 'L', 'A'])
    assert(find_ancestors(tree2, 'B')) == ['D', 'F']
    assert(find_ancestors(tree2, 3)) == []
    
if __name__ == "__main__":
    main()
