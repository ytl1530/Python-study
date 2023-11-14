# 1、使用 print 函数，将"人生苦短，我用python" 输出到 test.text 文件中

# str="人生苦短，我用python"

# fp = open('test.text','w')

# print(str,file=fp)

# fp.close()

# 2、使用 input 函数，从键盘输入姓名、年龄、座右铭，并使用 print 函数将内容输出到控制台

name = input('请输入姓名：')
age = input('请输入年龄：')
title = input('请输入座右铭：')

print('姓名' + name)
print('年龄'+ age)
print('座右铭'+ title)

