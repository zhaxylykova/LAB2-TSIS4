odds = 0
evens = 0
posnumbers = []
numbers = input()
for n in numbers.split():
    n = int(n)
    if n < 0:
        break
    posnumbers.append(n)
    

for i in range(len(posnumbers)):
    if posnumbers[i] % 2 == 0:
        evens+=1
    if posnumbers[i] % 2 != 0:
        odds+=1        
percentageofevens = 100 * evens / (evens + odds)
percentageofodds = 100 * odds / (evens + odds)
if percentageofevens == int(percentageofevens):
    percentageofevens = int(percentageofevens)
else:
    percentageofevens = round(percentageofevens, 4)    
if percentageofodds == int(percentageofodds):
    percentageofodds = int(percentageofodds)  
else:
    percentageofodds = round(percentageofodds, 4)       
answer = "{}% {}%"
print(answer.format(percentageofevens, percentageofodds))
