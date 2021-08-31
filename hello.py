# author: @zutlh
# datetime: 2021/8/29 0:03

# name = input("please enter your name:")
# print(name)
# print("hello", name)
# print(1024 * 768)
print('I\'m\"OK\"!')
print('I\'m learning python')
print(r'\\\d\a')
print(ord("A"))
print(ord("中"))
print(chr(100))
print('ABC'.encode("ascii"))
print('中文'.encode("utf-8"))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"))
print(len("中文"))
print(len("abc"))
# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len('中文'.encode("utf-8")))
print('hello %s' % 'world')
print('Hi, %s, you have $%d' % ('Micheal', 10000))
# list,可以存在不同的数据类型，其他和Java中差不多
classmates = ['micheal', 'tom']
print(classmates)
# tuple,另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates1 = ('micheal', 'tom')
print(classmates1)
age = 20
if age >= 18:
    print("your age is ", age)
    print("adult")
age1 = 3
if age1 >= 18:
    print('adult')
elif age1 >= 6:
    print('teenager')
else:
    print("kid")
    height = 1.75
    weight = 80.5
bmi = weight / (height * height)
print(bmi)
if bmi > 32:
    print('严重肥胖')
if 32 >= bmi >= 28:
    print('肥胖')
if 28 > bmi >= 25:
    print('过重')
if 25 > bmi >= 18.5:
    print('正常')
if bmi < 18.5:
    print('过轻')

