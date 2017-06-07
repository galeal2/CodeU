from BST import BST
from assignment_2_Q1 import find_ancestors

# find the lowest common ancestor
def find_common_ancestor(BT, node1, node2):
    """ the function takes a BST and two nodes from the tree
        and find their lowest common ancestor """
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
