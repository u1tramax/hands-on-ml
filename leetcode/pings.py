class RecentCounter:

    def __init__(self):
        self.requests = []
        self.cnt = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        lower_bound = t - 3000
        self.cnt += 1
        while self.requests[0] < lower_bound:
            self.cnt -= 1
            self.requests.pop(0)
        return self.cnt

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(642)
param_2 = obj.ping(1849)
param_3 = obj.ping(4921)
param_4 = obj.ping(5936)
print(param_1, param_2, param_3, param_4)