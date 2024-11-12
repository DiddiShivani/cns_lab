from Crypto.Cipher import DES3
from base64 import b64encode, b64decode
class DES:
    def __init__(self):
        self.my_encryption_key = 'ThisIsSecretEncryptionKey' 
        self.key = self.my_encryption_key.encode('utf-8')
        if len(self.key) < 24:
            self.key = self.key.ljust(24, b' ') 
        elif len(self.key) > 24:
            self.key = self.key[:24]  
        self.cipher = DES3.new(self.key, DES3.MODE_ECB)
    def encrypt(self, unencrypted_string):
        plain_text = unencrypted_string.encode('utf-8')
        while len(plain_text) % 8 != 0:
            plain_text += b' '
        encrypted_text = self.cipher.encrypt(plain_text)
        return b64encode(encrypted_text).decode('utf-8')
    def decrypt(self, encrypted_string):
        encrypted_text = b64decode(encrypted_string)
        decrypted_text = self.cipher.decrypt(encrypted_text).decode('utf-8')
        return decrypted_text.strip()  
message = input("Enter the string: ")
des_encryptor = DES()
encrypted_message = des_encryptor.encrypt(message)
decrypted_message = des_encryptor.decrypt(encrypted_message)    
print(f"\nString To Encrypt: {message}")
print(f"Encrypted Value: {encrypted_message}")
print(f"Decrypted Value: {decrypted_message}")







