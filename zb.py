def compare(x1, y1, x2, y2):
    dis1 = abs(x2 - x1)
    dis2 = abs(y2 - y1)
    if dis1 == dis2:
        return "YES"
    else:
        return "NO"    
    
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
print(compare(num1, num2, num3, num4))
