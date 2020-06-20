def convert(num):
    new = []
    if num == 0:
        return [0]
    while num:
        rem = num % 7
        new.append(rem)
        num = num // 7
    return new[::-1]

number = int(input())
for i in convert(number):
    print(i, end = "")    




