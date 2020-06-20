number = int(input())
array = list()
for i in range(number):
    t = int(input())
    array.append(t)
    double = t
    new = 0
    while t > 0:
        lastdigit = t % 10
        new = new * 10 + lastdigit
        t//=10
    if double == new:
        print("Yes") 
    else:
        print("No")
               
        

    