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


'''AES (Advanced Encryption Standard) is a symmetric encryption algorithm widely used for secure data encryption.
AES is both highly secure and efficient, making it suitable for a wide range of applications, including internet communications, financial data protection, and secure data storage.


1. Symmetric Encryption: Both encryption and decryption use the same secret key.
2. Block Cipher: AES operates on fixed-size blocks of data (128 bits).
3. Variable Key Length: AES supports key sizes of 128, 192, or 256 bits, allowing flexibility based on security needs.
4. Rounds: The algorithm involves multiple rounds of processing, with the number of rounds depending on the key size:
    128-bit key: 10 rounds
    192-bit key: 12 rounds
    256-bit key: 14 rounds'''


"""
1. SubBytes: Each byte in the state matrix is substituted with a corresponding byte from a fixed substitution table (S-box), enhancing non-linearity.
2. ShiftRows: Each row of the state matrix is shifted a certain number of positions to the left. This step ensures diffusion across rows.
3. MixColumns: Each column of the state matrix is transformed by a matrix multiplication, adding further diffusion.
4. AddRoundKey: The state matrix is XORed with the round key."""

