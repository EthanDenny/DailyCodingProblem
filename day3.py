class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize(data):
    if isinstance(data, str): data = data.splitlines()
    
    if len(data) == 0: return None
    if len(data) == 1: return Node(data[0].lstrip())

    left_indent = first_not_of(data[1], ' ')
    
    right_index = 2
    for line in data[2:]:
        this_indent = first_not_of(line, ' ')
        if this_indent == left_indent: break
        else: right_index += 1

    node = Node(data[0].lstrip(), deserialize(data[1:right_index]), deserialize(data[right_index:]))
    return node


def first_not_of(string, char):
    i = 0
    for c in string:
        if c == char: i += 1
        else: return i


def serialize(node, indent=0):
    data = ' ' * indent + node.val + '\n'
    if node.left: data += serialize(node.left, indent + 1)
    if node.right: data += serialize(node.right, indent + 1)
    return data


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
