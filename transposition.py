def columnarmat(mat,s):
    char = 0
    for i in range(r):
        for j in range(c):
            mat[i][j] = cipher[char]
            char+=1
            if char>=len(cipher):
                break
    s = []
    for char in key:
        for i in range(r):
            if mat[i][int(char)-1] != 0:
                s.append(mat[i][int(char)-1])
    return s

cipher = input("Enter the cipher text without spaces : ")
s = list(cipher)
r,c = map(int,input("Enter the rows and columns : ").split())
if r*c < len(cipher):
    print("Matrix size should be more than the length of the cipher :(")
else:
    mat = [[0]*c for _ in range(r)]
    n = int(input("Enter number of time you would like to iterate : "))
    for i in range(n):
        key = input("Enter the key whose length should be equal to columns : ")
        s = columnarmat(mat,s)
        print(''.join(s))