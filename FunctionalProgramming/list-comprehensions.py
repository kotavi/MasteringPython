import random

rnd = [random.random() for _ in range(10) if random.random() > 0.5]
print(rnd)

rnd = [x for x in [random.random() for _ in range(10)] if x > 0.5]
print(rnd)

rnd = [x for _ in range(10) for x in [random.random()] if x > 0.5]
print(rnd)
