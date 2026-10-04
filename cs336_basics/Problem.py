# Unicode1
## (a)
# chr(0) returns '\x00'
## (b)
# chr(0).__repr__() returns "'\\x00'". It makes '\x00' into a string, enabling  it to be printed 
print(chr(0) == None) # False
print(chr(0) == '') # False, chr(0) is string containing '\x00', '' is just empty.
print(len(chr(0)),len(''))
print(chr(0)=='\x00')
## (c)
# "this is a test"+ chr(0)+"string"  => 'this is a test\x00string'.  python print the repr of each char in the string.
print("this is a test"+ chr(0)+"string") # => this is a teststring. But print() returns the actual chars.

# Unicode2
utf8_encoded = "Hello,世界!😊".encode('utf-8')
print(utf8_encoded)
print(list(utf8_encoded))
print(len(utf8_encoded))
print(utf8_encoded.decode('utf-8'))
## (a)
# We can discrib all chars from combination of uft-8's. Models can recognize and output some chars whose using frequency is low but cannot be neglected. For example, "世" is encoded as \xe4\xb8\x96, and even an emoji "😊" => \xf0\x9f\x98\x8a
##(b)
# 'utf-8' codec can't decode byte 0xe4 in position 0: unexpected end of data
# When it comes to "世界", and the unicode of "世" is  \xe4\xb8\x96, but the wrong function try to decode them respectively.
## (c)
# \xe4\xb8 is the prefix code of a block of Chinese chars.




