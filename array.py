import array
from random import random
import time

# # saving and opening floats to/from file (quicker readin than other)
# # print(time.asctime())
# floats = array.array('d', (random() for i in range(10**7)))
# print(floats[-1])
# fp = open('floats.bin', 'wb')
# floats.tofile(fp)
# fp.close()
# floats2 = array.array('d')
# fp = open('floats.bin', 'rb')
# floats2.fromfile(fp, 10**7)
# fp.close()
# print(floats2[-1])
# print(floats2==floats)

# my_array = array.array('d', (i for i in range(12,10**3,121)))
# print(type(my_array))
# print(type(my_array[3]))
# print(len(my_array))
# print(my_array)

###mermoryview

# octets = array.array("B", range(6))
# m1 = memoryview(octets)
# print(m1.tolist())
# m2 = m1.cast('B', [2, 3])
# print(m2.tolist())
# m3 = m1.cast('B', [3, 2])
# print(m3.tolist())
# m2[1,1] = 22
# m3[1,1] = 33
# print(octets)
# print(m1.tolist())
# print(m3.tolist())
# print(len(m3))

numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])

memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)
