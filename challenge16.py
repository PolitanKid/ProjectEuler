value = str(pow(2,1000))


total = 0
for i in range(0,len(value)):
    v = value[i]

    total += int(v)

print(total)