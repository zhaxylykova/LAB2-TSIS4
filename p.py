def rectang(x1, y1, x2, y2,x3, y3):
    if x3 <= x2 and x3 >= x1 and y3 >= y2 and y3 <= y1:
        return "yes"
    else:
        return "no"    

number1, number2, number3, number4, number5, number6 = input().split()
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)
number4 = int(number4)
number5 = int(number5)
number6 = int(number6)
print(rectang(number1, number2, number3, number4, number5, number6))

