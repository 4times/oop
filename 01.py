class students():
    def __init__(self,age,gender,name,money,IQ):
        self.age = age
        self.gender = gender
        self.name = name
        self.money = money
        self.IQ = IQ
    def get_money(self):
        if self.money >= 10000:
            return '有钱人'
        else:
            return '穷逼'
    def get_IQ(self):
        return '九九乘法表'

liuzong = students(40,'刘总','男',100,1)
print(students.__dict__)
print(liuzong)
print(liuzong.money)
print(liuzong.get_money())
print(liuzong.age)
print(liuzong.name)
print(liuzong.get_IQ())
for i in range(1,10):
    for j in range(1,i+1):
        print('{}×{}={:<3}'.format(j,i,i*j),end='')
    print()
