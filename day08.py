# Taken from Day 3
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_unival_subtrees(node=None, root=True):
    if node == None:
        if root: return 0
        else: return 0, False

    if node.left == None and node.right == None:
        if root: return 1
        else: return 1, True
    
    left_count, left_is_unival = count_unival_subtrees(node.left, root=False)
    right_count, right_is_unival = count_unival_subtrees(node.right, root=False)
    
    count = left_count + right_count

    if left_is_unival and right_is_unival and (node.val == node.left.val == node.right.val):
        if root: return count + 1
        else: return count + 1, True
    
    if root: return count
    else: return count, False


if __name__ == "__main__":
    tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    assert count_unival_subtrees(tree) == 5
