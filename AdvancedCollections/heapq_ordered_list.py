import heapq

heap = [1, 3, 4, 2, 7, 8, 0, 5, 6]
heapq.heapify(heap)

print(heap)

print("The smallest element:", heap[0])
while heap:
    print(heapq.heappop(heap), heap)
    if len(heap) == 1:
        print("The largest element:", heap[0])
        break
