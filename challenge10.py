import math

primes = [2]

val = 3

while val < 2000000:
    is_prime = True
    sqrt_val = int(math.sqrt(val)) + 1

    for prime in primes:
        if prime > sqrt_val:
            break
        if val % prime == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(val)
    
    val += 2

print(sum(primes))