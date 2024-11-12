#ceaser cipher 
# pt = input("Enter the plain text : ")
# key = int(input("Enter the key : \n"))
# ct = ""
# for char in pt:
#     ct+=chr((ord(char)-97+key)%26+97)
# print(ct)

#ceaser cipher encryption
key = int(input("Enter number of shifts : "))
pt = input("Enter the plain text : ")
ct = ""
for char in pt:
    if char.isalpha():
        a = 97 if char.islower() else 65
        ct+=chr((ord(char) - a+key)%26+a)
print(ct)
#ceaser cipher decryption
dt= ""
for char in ct:
    if char.isalpha():
        a = 97 if char.islower() else 65
        dt+=chr((ord(char) -a-key)%26+a)
print(dt)