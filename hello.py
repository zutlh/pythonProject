# author: @zutlh
# datetime: 2021/8/29 0:03

# name = input("please enter your name:")
# print(name)
# print("hello", name)
# print(1024 * 768)

import collections
from collections.abc import Iterable

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
names = ['tom', 'micheal']
for name in names:
    print(name)
sum = 0
for x in [1, 2, 3, 4, 5]:
    sum += x
print(sum)
sum1 = 0
for x in list(range(100)):
    sum1 = sum1 + x
print(sum1)
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
# dict 相当于Java中的map
d = {'micheal': 99, 'tom': 29, 'jack': 89}
print(d)
print(d['micheal'])
print('tomas' in d)
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('micheal')
print(d)
# 和list比较，dict有以下几个特点：
#
# 1、查找和插入的速度极快，不会随着key的增加而变慢；
# 2、需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 1、查找和插入的时间随着元素的增加而增加；
# 2、占用空间小，浪费内存很少。

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 3])
s1 = set([2, 3, 4])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
print(s & s1)
a = ['c', 'b', 'a']
a.sort()
print(a)
a = 'ABC'
print(a.replace('A', 'a'))
print(a)
# 虽然字符串有个replace()方法，也确实变出了'Abc'，但变量a最后仍是'abc'，应该怎么理解呢？
# 我们先把代码改成下面这样：
a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)
# 上面我们讲了，str是不变对象，而list是可变对象。
# 要始终牢记的是，a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'：
# 所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
print(abs(100))
print(abs(-20))
print(max(1, 2, 3, 4))
a = abs
print(a(-1))
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print(move(100, 100, 60, math.pi / 6))
# 要注意定义可变参数和关键字参数的语法：
#
# *args是可变参数，args接收的是一个tuple；
#
# ** kw是关键字参数，kw接收的是一个dict
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])  # 切片 从0 到 3
print(L[-1])
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])
# 只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：
# 如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断：
print(isinstance('abc', Iterable))
# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
import os

print([d for d in os.listdir('.')])
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])
