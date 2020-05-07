from collections import OrderedDict

od = OrderedDict()
od['z'] = 3.4
od['x'] = 1
od['y'] = 34

print(od)

for k, v in od.items():
    print(k, v)

sorted_od = OrderedDict(sorted(od.items(), reverse=True, key=lambda kv: kv[1]))

print(sorted_od)
