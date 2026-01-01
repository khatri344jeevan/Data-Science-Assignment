#using libraries
from collections import deque

queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue:", list(queue))

dequeued_item = queue.popleft()
print("Dequeued:",dequeued_item)
print("Front element:",queue[0])