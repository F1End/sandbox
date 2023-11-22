# l = ["blah", "meh", "rofl", "meh", "mih", "mah", "mih", "meh", "blah",]
# print(set(l))
# print(list(set((l))))
#
# # remove duplicates but also keep order
# print(dict.fromkeys(l))
# print(list(dict.fromkeys(l).keys()))
#
# import time
#
# haystack = range(1, 10000000)
# needles = range(1, 100000000, 666)
# time1 = time.time()
# found = 0
# for n in needles:
#     if n in haystack:
#         found += 1
# time2 = time.time()
# found2 = len(set(needles) & set(haystack))
# time3 = time.time()
# haystack_set = set(haystack)
# needles_set = set(needles)
# time4 = time.time()
# found3 = len(needles_set & haystack_set)
# time5 = time.time()
# print("Time for loop:", time2-time1)
# print("Time for set:", time3-time2) # lol, ez sokkal hosszabb, van it valami magia a hatterbena loopnal, mert a konyv nem ezt mondja
# print("Time for set conversion:", time4 - time3)
# print("Time for purse set:", time5 - time4) #mostmar letszik, hogy ez gyorsabb picivel, mint a loop, de a konvertalas sokaig tart (az elonye, hogy egy sorba szepen befer)

s = {1}
print(s)
s.pop()
print(s)

f = frozenset(range(100))
print(f)

f_comp = {i**2 for i in range(10)}
print(f_comp)
frozen_comp = frozenset(i**2 for i in range(10))
print(frozen_comp)
"""Adding elements to a set may change the order of existing elements. That’s
because the algorithm becomes less efficient if the hash table is more than two-
thirds full, so Python may need to move and resize the table as it grows. When
this happens, elements are reinserted and their relative ordering may change."""

# operators
set_a = {"a", "b", "c", "d", 1, 2, 3}
set_b = {1, 2, 3, 4, 5, 6}
set_c = {1,2,3}

intersect = set_a & set_b
print(intersect)
union = set_a | set_b
print(union)
diff = set_a - set_b
print(diff)
symmetric_diff = set_a ^ set_b
print(symmetric_diff)
print(set_a.isdisjoint(set_b))
print("is it subset of?", set_b <= set_a)
print("is it subset of?", set_c <= set_b)
print("is it superset of?", set_a >= set_c)
# updating with differences (leaving diff only)
set_a -= set_b
print(set_a)
set_b.difference_update([4, 5])
print(set_b)

# dcitionary views (keys, items) szinten tud egy csomo hasonlo muveletet
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"a": 10, "b": 20}
print( d1.keys() & d2.keys())
print(type(d1.keys()))
print(type(d1.keys() & d2.keys()))
# dict_keys compatible with sets
print(d1.keys() | set_b)