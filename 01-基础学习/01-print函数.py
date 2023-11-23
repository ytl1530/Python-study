# print(value....,sep='', end= \n’,file=None)
'''
 value:代表要输出的值；
 逗号:代表输出的值可以为多个
 sep:输出的内容有空格是这个参数决定的
 end:输出的内容中有换行是由这个参数决定的
 file:如果想将输出的内容写到文件中，需要使用这个参数
'''

# 换行的输出
str = '150' # 字符串 str
num = 100 # 数字 num
print(num)
print(str)
print('''北京欢迎你！''')

# 不换行的输出
print(str,num,'要么出众，要么出丑')

# 输出ASCII码字符
print(chr(98),chr(91))

# 将内容输出到文件中
fp = open('node.text','w') # 打开文件
print('北京欢迎你！',file=fp) # 输出内容
fp.close() # 关闭文件

# 多个print函数输出为一行
print('hello',end='---')
print('word')

# 使用拼接符 ' + ' 链接字符串
print('hello' + 'word')