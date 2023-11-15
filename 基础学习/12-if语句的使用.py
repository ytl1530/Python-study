# if 分为 单分支、双分支和多分支

# 1、单分支
num = eval(input('请输入四位中奖号码：'))
if num == 9876:
    print('恭喜您中奖了！-------单分支')

if num != 9876:
    print('太遗憾了！您未中奖-------单分支')

# 2、双分支
if num == 9876:
   print('恭喜您中奖了！-------双分支')
else:
   print('太遗憾了！您未中奖-------双分支') 

# python 的三元运算符
result = '恭喜您中奖了！------- 三元运算' if num == 9876 else '太遗憾了！您未中奖 ------- 三元运算'
print(result)

# 3、多分支
if num == 9876:
    print('恭喜您中了一等奖！ -------- 多分支')
elif num==8765:
    print('恭喜您中了二等奖！ -------- 多分支')
elif num==7654:
    print('恭喜您中了三等奖！ -------- 多分支')
else:
    print('太遗憾了！您未中奖 ------- 多分支')

# 4、嵌套 if 的使用
talk = input('师傅，请吹一下酒精测试仪：')
if talk=='好':
    alcohol = eval(input('请输入测试数值：'))
    if alcohol>50:
        print('师傅！和我们走一趟吧')
    else:
        print('太遗憾了！')
else:
    print('想去陪陪凡凡？')

# 5、多条件 if 的使用

# 使用 and 操作符
user_name = input('请输入你的用户名：')
password = input('请输入你的密码：')

if user_name == 'zhangsan' and password == '666666':
    print('登录成功！')
else:
    print('用户名或密码错误')

# 使用 or 操作符
if num == 9876 or num==8765:
    print('恭喜您中奖了！ -------- or 操作符')
else:
    print('太遗憾了！您未中奖 ------- or 操作符')

# or 和 and 同时使用
if (user_name == 'zhangsan' or user_name == 'admin') and password == '666666':
    print('登录成功！')
else:
    print('用户名或密码错误')

# 6、模式匹配：3.11版本新特性
score = input('请输入用户成绩：')
match score:
    case 'A':
        print('还行')
    case 'B':
        print('不行')
    case 'C':
        print('差劲')
    case 'D':
        print('垃圾')