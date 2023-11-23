# break 退出循环，循环不执行

# 在 while 循环中的使用

# 1、累加和
i = 0  # 存储累加和的变量
n = 1  # 初始变量

while i<11:
    n+=i
    if n > 20:
        print('累加和：',n)
        break
    i+=1

# 2、登录
m = 0
while m < 3:
    user_name = input('请输入账号：')
    pwd = input('请输入密码：')
    if user_name == '123' and pwd == '666666':
        print('登录成功！')
        break
    else:
        if m < 2:
            print('您还有',2-m,'次机会！')
    m+=1
else:
   print('您的机会用完了！账户已冻结') 


# 在 for 循环中使用

for i in 'hello':
    print(i)
    if i == 'e':
        break
