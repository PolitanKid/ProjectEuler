current = 1
carry = 1
prev = 0
total = []

while current <= 4000000:
    if current % 2 == 0:
        total.append(current)
    prev = current
    current = current + carry
    carry = prev


print(sum(total))