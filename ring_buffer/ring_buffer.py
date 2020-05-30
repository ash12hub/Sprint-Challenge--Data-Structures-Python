class RingBuffer:
    def __init__(self, capacity):
        self.current_index = 0
        self.capacity = capacity
        self.buffer = []

    def append(self, item):
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
        else:
            self.buffer[self.current_index] = item
            self.current_index = (self.current_index + 1) % self.capacity

    def get(self):
        return self.buffer