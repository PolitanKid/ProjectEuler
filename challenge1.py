#Sum of all multiples of 3 or 5 below 1000

def sum(a,b):
    return (a + b)

values = []
total = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total = sum(total,i)

print(total)