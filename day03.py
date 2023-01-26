SEP_CH = '\t' # Seperating character. No node's val should contain this


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deserialize(data):
    if len(data) == 0: return None
    
    if isinstance(data, str):
        list_data = []
        i = 0; j = i
        while i < len(data):
            j = first_not_of(data, SEP_CH, j)
            if j < len(data):
                j = data.find(SEP_CH, j)
                if j == -1: j = len(data)
            else: j = len(data)
            list_data.append(data[i:j])
            i = j
        data = list_data
    
    val = data[0].replace(SEP_CH, '')
    
    if len(data) == 1:
        return Node(val)
    else:
        left_indent = first_not_of(data[1], SEP_CH)
        
        right_index = 2
        for line in data[2:]:
            this_indent = first_not_of(line, SEP_CH)
            if this_indent == left_indent: break
            else: right_index += 1

        node = Node(val, deserialize(data[1:right_index]), deserialize(data[right_index:]))
        return node


def first_not_of(string, char, start=0):
    i = start
    while i < len(string) and string[i] == char:
        i += 1
    return i


def serialize(node, indent=0):
    data = SEP_CH * indent + node.val
    if node.left: data += serialize(node.left, indent + 1)
    if node.right: data += serialize(node.right, indent + 1)
    return data


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
