def sumofdigits(n):
    if n != 0:
        return n % 10 + sumofdigits(n//10)
    else:
        return 0    

number = int(input())
lastdigit = number%10
summa = sumofdigits(number)
if summa % lastdigit == 0:
    print("Yes")
else:
    print("No")    