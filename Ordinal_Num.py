numbers = [value for value in range(1,10)]

for num in numbers:
    if num == 1:
        print(str(num) + "st ")
    elif num == 2:
        print(str(num) + "nd ")
    elif num == 3:
        print(str(num) + "rd ")
    elif num > 3:
        print(str(num) + "th ")