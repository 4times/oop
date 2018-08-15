class students():
    age = 18
    name = '名字'
    gender = 1

    def _money_(self):
        if self >= 10000 :
            print('有钱')
        else:
            print('穷逼')
liuzong = students()
print(liuzong.age)
print(students.__dict__)