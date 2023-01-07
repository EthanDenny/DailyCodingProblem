class LinkedList:
    class _Node:
        def __init__(self, elem=None):
            self.elem = elem
            self.next = None

    def __init__(self, elems=[]):
        self.head = None
        self.tail = None

        for e in elems:
            self.add(e)
    
    def add(self, elem):
        new = self._Node(elem)
        
        if self.head:
            self.tail.next = new
        else:
            self.head = new
        
        self.tail = new


def f(A, B):
    curr_A = A.head
    curr_B = B.head

    while curr_A.elem != curr_B.elem:
        curr_A = curr_A.next
        curr_B = curr_B.next
    
    return curr_A


if __name__ == "__main__":
    A = LinkedList([3, 7, 8, 10])
    B = LinkedList([99, 1, 8, 10])
    assert f(A, B).elem == 8
