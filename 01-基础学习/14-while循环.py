'''
    while 无限循环

    while 表达式:
        语句块

    while 表达式:
        语句块1 
    else: 
        语句块2
'''
# problem = input('今天上课吗？')
# while problem == '上':
#     print('你确定吗？')
#     problem = input('今天上课吗？')

# 1-100之间的累加和
# num = 0
# i = 1
# while i <= 100:
#     num+=i
#     i+=1
# else:
#     print(num)

# 模拟用户登录
# phone = input('请输入账号：')
# password = input('请输入密码：')
# i=0
# while i<2:
#     if phone != 'ytl' and password != '666666':
#         i=i+1
#         phone = input('请输入账号：')
#         password = input('请输入密码：')
#     else:
#         i=8
# else:
#     if phone == 'ytl' and password == '666666':
#         print('登录成功！')
#     else:
#         print('三次机会用完，已无法登录系统！')

# 使用嵌套循环打印图形
print('------------------------长方形--------------------------')
for i in range(1, 4):
    for n in range(1, 10):
        print('*', end='')
    print()

print('------------------------直角三角形--------------------------')
row = 1
for i in range(1, 6):
    row += 1
    for n in range(1, row):
        print('*', end='')
    print()
print('------------------------倒直角三角形--------------------------')
row = 6
for i in range(1, 6):
    for n in range(1, row):
        print('*', end='')
    row = row - 1
    print()

