my_tuple = (1,1,2)
# my_tuple = my_tuple * 2 + my_tuple

print((my_tuple))

print(hash(my_tuple))
print(my_tuple.count(1))
print(my_tuple[0])

my_tup_2 = tuple(range(1,10,2))
a, _, *rest, last = my_tup_2

print("a:", a)
print("rest:", rest)

div_tuple = (20, 4)
a, b = divmod(*div_tuple)

print(a)