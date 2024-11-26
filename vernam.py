def vernam_cipher_encrypt(plain_text, key):
	encrypted_text = ''.join([chr(ord(plain_text[i]) ^ ord(key[i])) for i in range(len(plain_text))])
	return encrypted_text

def vernam_cipher_decrypt(encrypted_text, key):
	decrypted_text = ''.join([chr(ord(encrypted_text[i]) ^ ord(key[i])) for i in range(len(encrypted_text))])
	return decrypted_text

# Example usage
plain_text = "HELLO"
key = "XMCKL"  # Key must be the same length as plain_text
encrypted_text = vernam_cipher_encrypt(plain_text, key)
decrypted_text = vernam_cipher_decrypt(encrypted_text, key)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
