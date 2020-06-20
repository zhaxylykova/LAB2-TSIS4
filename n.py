def addition(a, b):
    if a == b:
        return a + b
    if a > b:
        if b == 0:
            return a
        else:
            if b > 0:
                recurs = addition(a, b-1) + 1
                return recurs
            else:
                recurs = addition(a, b+1) - 1
                return recurs  
    if a < b:
        if a == 0:
            return b
        else:
            if a > 0:
                recurs = addition(a - 1, b) + 1
                return recurs
            else: 
                recurs = addition(a + 1, b) - 1
                return recurs    

            
number1, number2 = input().split()
number1 = int(number1)
number2 = int(number2)
answer = addition(number1, number2)
print(answer)
