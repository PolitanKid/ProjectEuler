#Largest Prime Factor of 600851475143
number = 600851475143

factors = []

for p in range(1,number):
    if number % p == 0:
        if (pow(2, p, p) - 2) % p == 0:
            v = (pow(2, p) - 2) // p
            if v % 2 == 0:
                factors.append(p)
                print(factors)
print(factors)