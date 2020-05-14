import operator
import functools
from collections import deque

print(dir(operator))
print(operator.mul)

result = functools.reduce(operator.mul, range(1, 6))
print(result)
result = functools.reduce(operator.mul, [1, 2, 3, 4, 5])
print(result)

f = operator.mul

result = f(f(f(f(1, 2), 3), 4), 5)
print(result)

iterable = deque(range(1, 6))
value = iterable.popleft()
while iterable:
    value = operator.mul(value, iterable.popleft())
print(value)
