#Largest Palindrome made from the product of two 3 digit numbers

num1 = 100
num2 = 100

palindromes = []

while num1 < 1000:
    product = num1 * num2
    product = str(product)
    if product[0] == product[-1] and product[1] == product[-2]:
        if len(product) == 5 or (len(product) == 6 and product[2] == product[-3]):
            palindromes.append(int(product))
    if num2 != 999:
        num2 += 1
    else:
        num1 += 1
        num2 = 100

palindromes.sort()

print(palindromes[-1])