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
