class RecentCounter:

    def __init__(self):
        self.queue = []
    def ping(self, t: int) -> int:
        self.queue.append(t)
        start_range = t - 3000
        while self.queue[0] < start_range:
            self.queue.pop(0)
        return len(self.queue)
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)