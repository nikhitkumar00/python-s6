n = int(input('Enter the number'))
tmp = 0
while n>0:
    temp = n%8
    tmp = tmp * 10 + temp
    n = n//8
string=str(tmp)
octalnum = string[::-1]
print(octalnum)