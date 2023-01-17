# Remove from Day 20
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
    
    # Remove the element after this one
    def remove_next(self, elem):
        if self.tail == elem.next:
            self.tail = elem
            self.tail.next = None
        else:
            elem.next = elem.next.next


# Remove the kth element from the end of the list (k=1 is the last element)
def f(link_list, k):
    curr = link_list.head
    pre_kth = None # The element before the kth from the end
    
    i = 0
    while curr != None:
        curr = curr.next
        if i == k: pre_kth = link_list.head
        if i > k: pre_kth = pre_kth.next
        i += 1
    
    link_list.remove_next(pre_kth)


if __name__ == '__main__':
    link_list = LinkedList()
    for i in range(10):
        link_list.add(i)
    
    f(link_list, k=1)
    f(link_list, k=5)
    f(link_list, k=7)

    # Convert linked list to array
    array = []
    curr = link_list.head
    while curr != None:
        array.append(curr.elem)
        curr = curr.next

    assert array == [0, 2, 3, 5, 6, 7, 8]
