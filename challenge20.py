total = 1

for i in range(1,101):
    total *= i

sumtotal = 0
for i in range(0,len(str(total))):
    sumtotal += int(str(total)[i])

print(sumtotal)