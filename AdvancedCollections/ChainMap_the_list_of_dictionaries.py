import argparse
import collections

defaults = {
    'key1': 'default key1 value',
    'key2': 'default key2 value'
}

parser = argparse.ArgumentParser()

parser.add_argument('--key1')
parser.add_argument('--key2')

args = vars(parser.parse_args())
filtered_args = {k: v for k, v in args.items() if v}

combined = collections.ChainMap(filtered_args, defaults, {'key1': 'val1'})

for map_ in combined.maps:
    print(map_.get('key1'))
    
print(args)
print(filtered_args)
print(combined)
print(combined['key1'])
