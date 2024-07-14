def triangle(a):
    return ((a*(a+1))/2)

def count_factors(b):
    count = 0
    sqrt = int(b**0.5)

    for i in range(1,sqrt + 1):
        if b % i == 0:
            count += 2
    if sqrt * sqrt == b:
        count -= 1
    return count

c = 1
while True:
    wf = triangle(c)

    if count_factors(wf) > 500:
        break
    
    c += 1

print(int(wf))