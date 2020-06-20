singlenumber = int(input())

cnt = 0
array = list(map(int, input().strip().split()))[:singlenumber]
height = int(input())
for i in range(singlenumber):
    if array[i] < height:
        cnt = cnt + 1

answer = singlenumber - cnt
print(answer)

