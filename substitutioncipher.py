key = 'qwertyuiopasdfghjklzxcvbnm'
pt = input("Enter the plain text : ")
ct = ''
for char in pt:
    ct+=key[ord(char)-97]
dt = ''
for char in ct:
    x = key.index(char)
    dt+=chr(x+97)
print(ct)
print(dt)