import heapq

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 3)

print("Heap:",heap)

min_item=heapq.heappop(heap)
print("Extracted min:",min_item)

print("Min element:",heap[0])