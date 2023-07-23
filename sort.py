list = []
for i in range(9999999999):
    list.append(i)

n = int(input("Enter the search element"))

for i in range(9999999999):
    if list[i] == n:
        print("Found at Location ",i)
        break