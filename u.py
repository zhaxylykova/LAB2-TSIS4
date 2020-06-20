a, b, x, y = input().split()
a = int(a)
b = int(b)
x = int(x)
y = int(y)

if (x >= a and y >= b) or (x >= b and y >= a):
    print("Thanks, Nurbek")
else:
    print("Impossible")    