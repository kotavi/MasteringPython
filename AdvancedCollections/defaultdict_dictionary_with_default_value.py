import pprint
from collections import defaultdict
import json

# List of connected nodes
nodes = (
    ('a', 'b'),
    ('a', 'c'),
    ('b', 'a'),
    ('c', 'a'),
    ('d', 'a'),
    ('d', 'b'),
    ('d', 'c'),
)
pprint.pprint(nodes)

dd = defaultdict(list)
for from_, to in nodes:
    dd[from_].append(to)
pprint.pprint(dd)


def tree():
    return defaultdict(tree)


colours = tree()
colours['other']['black'] = 0x000000
colours['other']['white'] = 0xFFFFFF
colours['primary']['red'] = 0xFF0000
colours['primary']['green'] = 0x00FF00
colours['primary']['blue'] = 0x0000FF
colours['secondary']['yellow'] = 0xFFFF00
colours['secondary']['aqua'] = 0x00FFFF
colours['secondary']['fuchsia'] = 0xFF00FF

print(json.dumps(colours, sort_keys=True, indent=4))

