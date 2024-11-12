from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii
def as_hex(byte_array):
    return binascii.hexlify(byte_array).decode('utf-8')


message = "AES still rocks!!"
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_ECB)
encrypted = cipher.encrypt(pad(message.encode(), AES.block_size))
print("Encrypted string: " + as_hex(encrypted))


cipher_dec = AES.new(key, AES.MODE_ECB)
decrypted = unpad(cipher_dec.decrypt(encrypted), AES.block_size)
original_string = decrypted.decode('utf-8')
print("Original string: " + original_string + " " + as_hex(decrypted))

