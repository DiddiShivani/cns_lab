def vigenere_encrypt(text, key):
	key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
	encrypted_text = ''.join([chr(((ord(text[i]) + ord(key[i])) % 26) + 65) for i in range(len(text))])
	return encrypted_text

def vigenere_decrypt(encrypted_text, key):
	key = key * (len(encrypted_text) // len(key)) + key[:len(encrypted_text) % len(key)]
	decrypted_text = ''.join([chr(((ord(encrypted_text[i]) - ord(key[i]) + 26) % 26) + 65) for i in range(len(encrypted_text))])
	return decrypted_text

# Example usage
text = "HELLO"
key = "KEY"
encrypted = vigenere_encrypt(text, key)
decrypted = vigenere_decrypt(encrypted, key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
