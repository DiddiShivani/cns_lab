#xor with zero
st = "Hello World"
res = ''.join([chr(ord(char)^0) for char in st])
print(res)

res_and = ''.join([chr(ord(char)&127) for char in st])
res_or = ''.join([chr(ord(char)|127) for char in st])
res_xor = ''.join([chr(ord(char)^127) for char in st])
print(res_and)
print(res_or)
print(res_xor)