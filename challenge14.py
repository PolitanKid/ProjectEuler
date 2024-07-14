greatestcount = 0
for a in range(1,1000001):
    count = 1
    i = a
    while i != 1:
        if i % 2 == 0:
            i = i//2
            # print(f"Even {i}")
        else:
            i = (i*3)+1
            # print(f"Odd {i}")
        
        count += 1
    # print(f"Count {count}")
    # print("\n")
    # print("\n")

    if count > greatestcount:
        greatestcount = count
        greatestinput = a
    print(f"Count for {a} is {count} and the best count so far is {greatestcount} which came from {greatestinput}")


print(greatestcount)