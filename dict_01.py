#
#
# dial_codes = [(880, "Bangladesh"), (55, "Brazil"), (36, "Hungary"), (81, "Japan")]
# country_dial = {code:country for code, country in dial_codes}
# print(dial_codes)
#
# country_dial_2 = {country.upper(): str(code) for code, country in dial_codes if code < 82}
# print(country_dial_2)
#
# def dump(**meh):
#     return meh
#
# print(dump(**{'x': 1}, y=2, **{'z': 3}, xb=2))
#
# def dump2(*mahargs):
#     return mahargs
#
# print(dump2("a", *[1,2], *{"a": 33}))
#
#
# print({'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'm': 4}})
#
# #only python 3.9 or neweer
# d1 = {'a': 1, 'b': 3}
# d2 = {'a': 2, 'b': 4, 'c': 6}
# print(d1 | d2)
# d1 |= d2
# print(d1)
#
#
# ###case matching
#
# def get_creators(record: dict) -> list:
#     match record:
#         case {'type': 'book', 'api': 2, 'authors': [*names]}:
#             return names
#         case {'type': 'book', 'api': 1, 'author': name}:
#             return name
#         case {'type': 'book'}:
#             raise ValueError(f"Invalid book record: {record!r}")
#         case {'type': 'movie', 'director': name}:
#             return [name]
#         case _:
#             raise ValueError(f'Invalid record: {record!r}')
#
# b1 = dict(api=1, author='Douglas Hofstadter', type="book", title="Godel, Escher, Bach")
# print(b1)
# print(get_creators(b1))
# from collections import OrderedDict
# b2 = OrderedDict(api=2, type="book", title="Python in a Nutshell", authors="Martelli Ravencscroft Holden".split())
# print(b2)
# print(get_creators(b2))
# # get_creators({'type': 'book'})
# get_creators(333333)
#
# #In contrast with sequence patterns, mapping patterns succeed on partial matches (e.g. title in b1/b2)
#
#
from collections import abc
my_dict = {}
print(isinstance(my_dict, abc.Mapping))
print(isinstance(my_dict, abc.MutableMapping))