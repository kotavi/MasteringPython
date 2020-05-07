"""
bisect module:
 - if your primary purpose is searching
 - works on a standard list
 - adding items to the list O(n)
 - creating sorted list O(n*n)
"""

import bisect

sorted_list = []
bisect.insort(sorted_list, 5)
bisect.insort(sorted_list, -1)
bisect.insort(sorted_list, 0)
bisect.insort(sorted_list, 6)
bisect.insort(sorted_list, 7)
bisect.insort(sorted_list, 1)

print(sorted_list)


def my_contains(lst, value):
    i = bisect.bisect_left(lst, value)
    return i < len(sorted_list) and lst[i] == value


print(my_contains(sorted_list, 5))
print(my_contains(sorted_list, 7))
print(my_contains(sorted_list, 6))
print(my_contains(sorted_list, 1))
print(my_contains(sorted_list, 2))
