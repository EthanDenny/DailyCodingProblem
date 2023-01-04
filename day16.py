class Log:
    class _Order:
        id = None
        previous = None

        def __init__(self, id, previous):
            self.id = id
            self.previous = previous

    def __init__(self):
        self._newest = None

    def record(self, order_id):
        self._newest = self._Order(order_id, self._newest)

    def get_last(self, i):
        curr = self._newest
        for n in range(i-1):
            curr = curr.previous
        return curr.id


if __name__ == "__main__":
    order_log = Log()
    
    order_log.record('A')
    order_log.record('B')
    order_log.record('C')
    order_log.record('D')
    order_log.record('E')

    assert order_log.get_last(5) == 'A'
