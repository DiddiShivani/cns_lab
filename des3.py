from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

key = DES3.adjust_key_parity(get_random_bytes(24))

def des3_encrypt(key,data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_data = data + (8-len(data)%8)*' '
    encrypted_data = cipher.encrypt(padded_data.encode())
    return encrypted_data

def des3_decrypt(key,en_data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_data = cipher.decrypt(en_data).decode().rstrip()
    return decrypted_data

data  = 'Shivani'
en_data = des3_encrypt(key,data)
print(en_data)
de_data = des3_decrypt(key,en_data)
print(de_data)
