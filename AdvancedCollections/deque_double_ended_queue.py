"""
Internally deque is created as a doubly linked list
"""

from collections import deque

queue = deque()

for i in range(-5, 6):
    queue.append(i)

print(queue)

queue.popleft()
queue.popleft()
queue.popleft()

print(queue)

queue.pop()
queue.pop()
queue.pop()

print(queue)
print("* - * -" * 20)

another_queue = deque(maxlen=2)
for i in range(-5, 6):
    another_queue.append(i)
    print(another_queue)