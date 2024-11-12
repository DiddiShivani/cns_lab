import math

'''
1. take p and q (large prime numbers)
2. find n = p*q
3. phi(n) = (p-1)*(q-1)
4. find e such that 1 < e < phi(n) and gcd(e, phi(n)) == 1
5. find d such that d * (emod(phi(n))) = 1
6. encrypt the message using c = m^e mod n
7. decrypt the message using m = c^d mod n
'''

import math 
p = 3
q = 7
n = p*q
print("n =", n)
phi = (p-1)*(q-1)
print("phi = ",phi)
e = 2
while(e<phi):
    if (math.gcd(e, phi) == 1):
        break
    else:
        e += 1
print("e =", e)
j = 0
while(j<phi):
    if (j*e%phi == 1):
        d = j
        break 
    j+=1
print("d =", d)
print(f'Public key: {e, n}')
print(f'Private key: {d, n}')
msg = 11
print(f'Original message:{msg}')
C =(msg**e)%n
print(f'Encrypted message: {C}')
M = (C**d)%n
print(f'Decrypted message: {M}')