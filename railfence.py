# Encryption
def rail_fence_encrypt(text, key):
    rails = ['' for _ in range(key)]
    direction_down = False
    row = 0
    for char in text:
        rails[row] += char
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
    return ''.join(rails)

# Decryption
def rail_fence_decrypt(encrypted_text, key):
    n = len(encrypted_text)
    zigzag = [['\n' for _ in range(n)] for _ in range(key)]
    direction_down = None
    row, col = 0, 0
    for i in range(n):
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False
        zigzag[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1
    index = 0
    for i in range(key):
        for j in range(n):
            if zigzag[i][j] == '*' and index < n:
                zigzag[i][j] = encrypted_text[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(n):
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False
        if zigzag[row][col] != '\n':
            result.append(zigzag[row][col])
            col += 1
        row += 1 if direction_down else -1
    return ''.join(result)

text = "HELLO RAIL FENCE"
key = 3
encrypted = rail_fence_encrypt(text, key)
decrypted = rail_fence_decrypt(encrypted, key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
