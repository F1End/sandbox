my_string = "Bro barbary bribes"
print(my_string[::2])
print(my_string[-2::-3])

invoice = """
... 0.....6.................................40........52...55........
... 1909  Pimoroni PiBrella                     $17.50    3    $52.50
... 1489  6mm Tactile Switch x20                 $4.95    2     $9.90
... 1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
... 1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
... """

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
TOTAL = slice(55, None)

line_items = invoice.split("\n")[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION], item[TOTAL])

my_new_value = [i for i in range(101)]
print(my_new_value[TOTAL])

my_new_value[TOTAL] = my_new_value[TOTAL].__reversed__()
print(my_new_value)

# a * n on mutable items will reference the same mutable n times

# good
board = [["_"] * 3 for i in range(3)]
print(board)
board[0][2] = "X"
print(board)

# bad
board_bad = [["_"] * 3] * 3
print(board_bad)
board_bad[0][2] = "o"
print(board_bad)


# += and *= will append the same instance (if __iadd__ and __imul__ are implemented for mutable sequences
# if not implemented or not mutable, will fall back to a = a + b, which will create a new object is created
# -> doing this repeatedly to immutable items is not efficient due to extra copying; except for str, as it is optimizesd
# for that use (due to expected high use), leaving extra memory for str, not needing copy each time
my_list = [1, 2, 3]
print(id(my_list))
my_list *= 2
print(id(my_list))
my_tuple = (1, 2, 3)
print(id(my_tuple))
my_tuple *= 2
print(id(my_tuple))

# weird += behaviour
my_weird_tuple = (1, 2, [30, 40])
try:
    my_weird_tuple[2] += [50, 60]
except TypeError as e:
    print(e)
print(my_weird_tuple)
