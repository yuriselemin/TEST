

def cycle_num(list):
    total = []
    for i in list:
        total.append(i + (i+1))
        print(total)

list = range(1, 11)
print(''.join(str(x) for x in list))







print(*range(1,11))



print(''.join(str(x) for x in range(1, 11)))









