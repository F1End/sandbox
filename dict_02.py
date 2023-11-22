# from collections import ChainMap, Counter
#
#
# d1 = dict(a=1, b=2)
# d2 = {"a": 66, "b": 33, "c": 44}
# d_chain = ChainMap(d1, d2)
# print(d_chain["a"])
# print(d_chain["c"])
#
# d_chain["c"] = 3
# print(d_chain["c"])
# print(d1)
#
# import builtins
#
# pylookup = ChainMap(locals(), globals(), vars())
# print(pylookup)
#
#
# d3 = d1.pop("a")
# print(d3)
# print(d1)
# print(d2.pop("d", "Not found"))
#
# my_counter = Counter("abracadabra")
# print(my_counter)
# my_counter.update("blahahaaaa")
# print(my_counter)
# print(my_counter.most_common(3))

import collections


class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy[1])
# d_proxy[1] = "X"
d[2] = "B"
print(d_proxy)

my_dict = dict(a=10, b=20, c=30)
print(my_dict)
values = my_dict.values()
print(values)
print(len(values))
print(list(values))
reversed(values) # szerintem ez nem is mukodik; 3.6 errot dob, itt meg nem latok valtozast
print(values)
print(values[0])

