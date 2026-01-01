def create_heap():
    return []

def is_empty(heap):
    return len(heap) == 0

def insert(heap, item):
    heap.append(item)
    print("Inserted:", item)
    heap.sort()

def extract_min(heap):
    if is_empty(heap):
        return "Heap is empty"
    return heap.pop(0)

def peek(heap):
    if is_empty(heap):
        return "Heap is empty"
    return heap[0]
    
heap = create_heap()
insert(heap, 10)
insert(heap, 5)
insert(heap, 20)
insert(heap, 3)

print("Extracted min:", extract_min(heap))
print("Heap:", heap)
print("Min element:", peek(heap))