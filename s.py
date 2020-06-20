def check(a, b, string):
    size = a+b+1
    sum = 0
    if size != len(string):
        return "No"
    if string[a] != "-":
        return "No"
    for i in range(0, a):
        if string[i] >="0" and string[i] <= "9":
            sum += 1
    for i in range(a + 1, size):
        if string[i] >= "0" and string[i] <="9":
            sum += 1
    if(sum != size - 1):
        return "No"
    else:
        return "Yes"   
         
number1, number2 = input().split()
number1 = int(number1)
number2 = int(number2)
code = str(input())
print(check(number1, number2, code))
