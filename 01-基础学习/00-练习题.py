# 1、使用 print 函数，将"人生苦短，我用python" 输出到 test.text 文件中

# str="人生苦短，我用python"

# fp = open('test.text','w')

# print(str,file=fp)

# fp.close()

# 2、使用 input 函数，从键盘输入姓名、年龄、座右铭，并使用 print 函数将内容输出到控制台

# name = input('请输入姓名：')
# age = input('请输入年龄：')
# title = input('请输入座右铭：')

# print('姓名' + name)
# print('年龄'+ age)
# print('座右铭'+ title)
 
# 3、从键盘上输入4位的整数，分别输出 个位，十位，百位，千位 的数值，使用 eval 函数或者 int 函数将从键盘获取的字符串转为 int 类型，通过整除和取余操作分别获取数字
# 方法一：
# num = eval(input('请输入四位的数字：'))
# print('个位上的数：',num%10)
# print('十位上的数：',num//10%10)
# print('百位上的数：',num//100%10)
# print('千位上的数：',num//1000)

# 方法二：
# num2 = input('请输入四位的数字：')
# print('个位上的数：',num2[3:4])
# print('十位上的数：',num2[2:3])
# print('百位上的数：',num2[1:2])
# print('千位上的数：',num2[0:1])

# 4、根据父母身高预测儿子身高，从键盘输入父母身高，并使用 eval 函数或者 float 函数转换输入的类型，计算公式 儿=（父+母）* 0.54

# fu = eval(input('请输入父亲的身高：'))
# mu = eval(input('请输入母亲的身高：'))
# son = (fu+mu)*0.54
# print(round(son,1))

# 5、输入一个年份判断是否是闰年：能被4整除但不能被100整除 或 能被400整除
# year = eval(input('请输入年份：')) 
# if 400%year==0 or (year%4==0 and year%100!=0):
#     print(year,'是闰年')

# 6、模拟10086查询功能：输入1显示余额，输入2显示流量，输入3显示通话时间，输入0退出
# print('1：查询余额')
# print('2：查询流量')
# print('3：查询通话时间')
# print('0：退出查询')
# num = eval(input('请输入查询数值：'))
# while num < 4:
#     if num == 0:
#         break
#     elif num == 1:
#         print('话费余额为：10.00元')
#     elif num == 2:
#         print('剩余流量为：10G')
       
#     elif num == 3:
#         print('通话时间为：100分钟')
#     num = eval(input('请输入查询数值：'))
# else:
#     print('请输入正确的查询数值')
#     num = eval(input('请输入查询数值：'))

# 7、打印出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i) + '*' + str(j) + '=' + str(i*j),end='\t')
    print()