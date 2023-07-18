f = open("caesor.txt","r")
nf = open("cipher.txt","w")

n = int(input("Enter the encoding number : "))

for line in f:
    for letter in line:
        if letter != " ":
            char = ord(letter)
            newchar = char + n
            nf.write(chr(newchar))
        else:
            nf.write(" ")

f.close()
nf.close()