#Smallest Number divisible by 1-20
value = 20
result = 0

while True:
    if value % 20 == 0 and value % 19 == 0 and value % 18 == 0 and value % 17 == 0 and value % 16 == 0 and value % 15 == 0 and value % 14 == 0 and value % 13 == 0 and value % 12 == 0 and value % 11 == 0 and value % 10 == 0 and value % 9 == 0 and value % 8 == 0 and value % 7 == 0 and value % 6 == 0 and value % 5 == 0 and value % 4 == 0 and value % 3 == 0 and value % 2 == 0 and value % 1 == 0:
        print(value)
        break
    value += 1

