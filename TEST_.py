

def cycle_num(list):
    total = []
    for i in list:
        total.append(i + (i+1))
        print(total)

list = range(1, 11)
print(''.join(str(x) for x in list))


print(*range(1,11))


print(''.join(str(x) for x in range(1, 11)))




class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_info(self):
        print(f'Привет! меня зовут {self.name} и мне {self.age} года')

    def birthday(self):
        self.age += 1
        print(f'Привет, у меня сегодня день рождения. Мне  {self.age} года')


den = Human('Денис', age=22)
max = Human('Макс', age=22)


print(den.name, den.age)
print(max.name, max.age)
den.say_info()
max.say_info()
den.birthday()


list1 = []
list2 = []

for num in range(10):
    if num % 2 == 0:
        list1.append(num)
    else:
        list2.append(num)

list11 = '*'.join(map(str,list1))
list22 = '*'.join(map(str,list2))
print(*list22)
print(*list11)





