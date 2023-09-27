from collections import abc

list_1 = ["a", "b", "c"]
tuple_1 = ("a","e","g")

tuple_2 = tuple(list_1)

list_1.reverse()
print(list_1)

# list_2 = list_1.__reversed__()
print(reversed(tuple_1))

class MyCustomList:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

    def __reversed__(self):
        return reversed(self.data)

# Create an instance of the custom class
my_list = MyCustomList([1, 2, 3, 4, 5])

# Use the reversed() function on the custom object
for item in reversed(my_list):
    print(item)


"""Generators"""

import array


my_array = array.array("I", (n**2 for n in range(1,11,3)))
print(my_array)




print(tuple_2[0])