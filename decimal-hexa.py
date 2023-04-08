n = int(input('Enter the number'))
tmp = ''
while n > 0:
    temp = n % 16
    if n > 9:
        num = n-9
        tmp = str(ord(num) + 65)
    tmp = tmp + str(temp)
    n = n // 16
string=str(tmp)
hexa = string[::-1]
print(hexa)