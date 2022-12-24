pointers = {}


def get_pointer(obj):
    return id(obj)


def dereference_pointer(address):
    if address == 0:
        return None
    else:
        return pointers[address]


class XORLinkedList:
    class _Node():
        val = None
        both = 0

        def __init__(self, val=None, both=0):
            self.val = val
            self.both = both

            pointers[id(self)] = self
    
    _head = None
    _tail = None
    _count = 0

    def __init__(self):
        pass

    def add(self, element):
        if self._count == 0:
            self._head = self._Node(element)
            self._tail = self._head
        elif self._count == 1:
            self._tail = self._Node(element, get_pointer(self._head))
            self._head.both = get_pointer(self._tail)
        else:
            old_tail = self._tail
            self._tail = self._Node(element, get_pointer(old_tail))
            old_tail.both ^= get_pointer(self._tail)
        
        self._count += 1
    
    def get(self, index):
        i = 0
        last_ptr = 0
        node = self._head
        while i < index:
            next_ptr = last_ptr ^ node.both
            last_ptr = get_pointer(node)
            node = dereference_pointer(next_ptr)
            i += 1
        return node


if __name__ == "__main__":
    n = XORLinkedList()

    n.add('A')
    n.add('B')
    n.add('C')
    n.add('D')
    n.add('E')

    assert n.get(0).val == 'A'
    assert n.get(1).val == 'B'
    assert n.get(2).val == 'C'
    assert n.get(3).val == 'D'
    assert n.get(4).val == 'E'
