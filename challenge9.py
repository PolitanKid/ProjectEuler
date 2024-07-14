import math

finished = False

a = 0
b = 1

pytrips = []

while finished != True:
    a += 1
    if str(math.sqrt((a**2 + b**2)))[-1] == "0" and str(math.sqrt((a**2 + b**2)))[-2] == ".":
        if a + b + math.sqrt((a**2 + b**2)) == 1000:
            print(f"{a},{b},{int(math.sqrt((a**2 + b**2)))}")
            
            print("Answer is " + str(a*b*math.sqrt((a**2 + b**2))))
            break

    else:
        if a == 1000:
            a = 1
            b += 1