class HitCounter:
    hits = []

    def record(self, timestamp) -> None:
        self.hits.append(timestamp)

    def total(self) -> int:
        return len(self.hits)

    def range(self, lower, upper) -> int:
        return sum(1 for t in self.hits if lower <= t <= upper)
