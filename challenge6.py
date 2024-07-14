#Sum of Sqquares - Square of Sum of 1-100
squareofsum = 0
sumofsquares = 0

for v in range(1,101):
    #Sum of Squares
    sumofsquares += (v**2)

    #Square of Sum
    squareofsum += v
    print(f"{v}     {sumofsquares} / {squareofsum}")
    if v == 100:
        squareofsum = squareofsum**2
    
print(squareofsum-sumofsquares)