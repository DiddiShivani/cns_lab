from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
def encrypt_bf(inp_file,out_file):
    key = get_random_bytes(16)
    c = Blowfish.new(key,Blowfish.MODE_CFB)
    iv = c.iv
    with open(inp_file,"rb") as fin, open(out_file,'wb') as fout:
        while True:
            chunk = fin.read(64)
            if not chunk:
                break
            fout.write(c.encrypt(chunk))
    return key,iv
def decrypt_bf(key,iv,en_file,de_file):
    c = Blowfish.new(key,Blowfish.MODE_CFB,iv=iv)
    with open(en_file,"rb") as fin, open(de_file,'wb') as fout:
        while True:
            chunk = fin.read(64)
            if not chunk:
                break
            fout.write(c.decrypt(chunk))
inp_file = "inpFile.txt"
en_file = "encryptedFile.txt"
dec_file = "decryptedFile.txt"
k,iv= encrypt_bf(inp_file,en_file)
decrypt_bf(k,iv,en_file,dec_file)
