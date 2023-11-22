# s = 'café'
# print(len(s))
# b = s.encode('utf8')
# print(b)
# print(len(b))
# print(b.decode())



# cafe = bytes('café', encoding='utf8')
# print(cafe)
# print(cafe[0])
# print(cafe[:1]) # a slice of a binary sequence always producesa binary sequence of the same type
# cafe_arr = bytearray(cafe)
# print(cafe_arr)
# print(cafe_arr[0:1]) # a slice of a binary sequence always producesa binary sequence of the same type
# print(type(cafe[0]))
# print(type(cafe[0:1])) # a slice of a binary sequence always producesa binary sequence of the same type
#
# print(bytes.fromhex('31 4B CE A9').decode())


# import array
# numbers = array.array('h', [-2, -1, 0, 1, 2])
# octets = bytes(numbers)
# print(numbers)
# print(octets)
#
# for codec in ['latin_1', 'utf_8', 'utf_16', 'utf-16le','cp1252', 'gb2312', 'cp437']:
#     print(codec, 'Café'.encode(codec), sep='\t')
#
# city = 'São Paulo'
# # print(city.encode('cp437'))
# print(city.encode('cp437', errors='ignore'))
# print(city.encode('cp437', errors='replace'))
# print(city.encode('cp437', errors='xmlcharrefreplace'))
#
# # The codecs error handling is extensible. You may register extra
# # strings for the errors argument by passing a name and an error
# # handling function to the codecs.register_error function. See the
# # codecs.register_error documentation.



octests = b'Montr\xe9al'
print(octests.decode('cp1252'))
print(octests.decode('iso8859_7'))
print(octests.decode('koi8_r'))
# print(octests.decode('utf_8'))
print(octests.decode('utf_8', errors='replace'))
print(list(octests))
little_endian = 'Montréal'.encode('utf_16le')
big_endian = 'Montréal'.encode('utf_16be')
print(list(little_endian))
print(list(big_endian))

# When writing, I recommend
# using UTF-8 for general interoperability. For example, Python
# scripts can be made executable in Unix systems if they start with
# the comment: #!/usr/bin/env python3. The first two bytes of the
# file must be b'#!' for that to work, but the BOM breaks that con‐
# vention.