import os
os.system("cls")

speed = {
    "Tesla": 250,
    "BMW": 240,
    "Mercedes": 260,
    "Audi": 230
}

lst = []
for k,v in speed.items():
    
        for i in range(len(lst)):
            if lst[i][1] > v:
                lst.insert(i, [k,v])
                break
        else:
            lst.append([k,v])
            
print(lst[::-1])

