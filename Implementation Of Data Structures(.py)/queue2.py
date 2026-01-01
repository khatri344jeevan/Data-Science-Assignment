#implementation without using libraries
def create_queue():
    queue = []
    return queue

def is_empty(queue):
    return len(queue) == 0

def enqueue(queue, item):
    queue.append(item)
    print("Enqueued:", item)

def dequeue(queue):
    if is_empty(queue):
        return "Queue is empty"
    return queue.pop(0)

def peek(queue):
    if is_empty(queue):
        return "Queue is empty"
    return queue[0]
    

q=create_queue()
enqueue(q,10)
enqueue(q,20)
enqueue(q,30)

print("Dequeued:",dequeue(q))
print("Queue:",q)
print("Front element:", peek(q))