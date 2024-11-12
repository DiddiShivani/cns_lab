n,g,x,y = map(int,input("Enter the values of n,g,x,y : ").split())
#A is alice public key and B is Bob public key
A = (g**x) % n
B = (g**y) % n
k1 = (B**x) % n
k2 = (A**y) % n
print("Alice public key : ",A)
print("Bob public key : ",B)
print("Shared secret(Alice) : ",k1)
print("Shared secret(Bob) : ",k2)