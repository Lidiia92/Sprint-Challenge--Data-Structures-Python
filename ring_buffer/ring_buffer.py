class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current == self.capacity:
      self.current = 0

    if self.current < self.capacity:
      self.storage[self.current] = item
      self.current += 1

  def get(self):
    storage = []
    for value in self.storage:
      if value:
        storage.append(value)
    return storage


buffer = RingBuffer(3)

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')

print(buffer.get())