
total = 0

while True:
    try:
        income = int(input("Please enter your income: "))
    except ValueError:
        print("Please enter your income as a number")
        continue
    else:
        break

if (income - 10) > 0:
    total += (income/10)
    income -= 10
else:
    print (income)

if (income - 10) > 0:
    total += (income/20)
    income -= 10
else:
    print (income)


if (income - 10) > 0:
    total += (income/30)
    income -= 10
else:
    print (income)


if (income - 10) > 0:
    total += (income/40)
    income -= 10
else:
    print (income)
    

if (income - 10) > 0:
    total += (income/50)
    income -= 10
else:
    print (income)


if (income - 10) > 0:
    total += (income/60)
    income -= 10
else:
    print (income)

print (total)
