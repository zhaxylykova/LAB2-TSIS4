def isBackHome(line):
    cnt1 = 0
    cnt2 = 0
    size = len(line)
    for i in range(0, size):
        if line[i] == "U":
            cnt1+=1
        if line[i] == "D":
            cnt1-=1
        if line[i] == "L":
            cnt2+=1
        if line[i] == "R":
            cnt2-=1
    if cnt1 == 0 and cnt2 == 0:
        return "True"
    return "False"     
 
line = str(input())
print(isBackHome(line))

