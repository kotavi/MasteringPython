from datetime import datetime, timedelta
from itertools import cycle


def timestamp_to_str(value):
    return value.strftime("%Y-%m-%dT%H:%M:%S.000Z")


_now1day = [timestamp_to_str(datetime.now() + timedelta(minutes=i)) for i in range(1, 2400, 25)]
print(_now1day)
now1day = cycle(_now1day)
print(next(now1day))
for i in range(len(_now1day) * 2):
    print(next(now1day))

