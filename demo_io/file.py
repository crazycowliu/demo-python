#!/usr/bin/python3
import binascii
 
print ("Hello, Python3!")

file_object = open('.\\input.\\key.txt')
try:
    all_the_text = file_object.read()
    print (all_the_text)
finally:
    file_object.close()

file_object = open('.\\input.\\key', 'rb')
try:
    while True:
        chunk = file_object.read(16)
        if not chunk:
            break
#         print(chunk)
        print(binascii.b2a_hex(chunk))
finally:
    file_object.close()

b = b"example"                  # bytes object 
print(b)
s = str(b, encoding = "utf-8")  # bytes to str
print(s)

s = "example"                   # str object 
b = bytes(s, encoding = "utf8") # str to bytes 
print(b)

b = str.encode(s)               # str to bytes 
print(b)
s = bytes.decode(b)             # bytes to str 
print(s)

hex_str = '0123456789ABCDEF'
byte_arr = bytearray.fromhex(hex_str)
s = binascii.b2a_hex(byte_arr)
print(s)