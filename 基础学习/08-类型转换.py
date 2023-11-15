# 类型转换：隐式类型转换、显式类型转换

# 1、隐式转换
x = 10 # 类型：<class 'int'>
y = 3  # 类型：<class 'int'>
x/y,type(x/y) # 输出：3.3333333333333335 类型：<class 'float'>

# 2、显式转换

# 2.1、int() 将其他字符转换为整数类型
z = '10'
int(z) # 输出：10
a=3.14 
int(a) # 输出：3

# 2.2、float() 将其他字符转换为浮点类型
b = '12' 
float(b) # 输出：12.0  类型：<class 'float'>
c = 2
float(c) # 输出：2.0   类型：<class 'float'>

# 2.3、str() 将其他字符转为字符串
d = 10
e = 3.14
str(d) # 输出：10   类型：<class 'str'>
str(e) # 输出：3.14 类型：<class 'str'>

# 2.4、ord() 将一个 unicode 中对应的字符转换为整数
f = '尹'
ord(f) # 输出：23609

# 2.5、chr() 将一个整数转换为 unicode 中对应的字符
g = 23609
chr(g) # 输出：尹

# 2.6、hex() 将一个整数转换为十六进制的字符串
h = 10
hex(h),type(hex(h)) # 输出：0xa  类型：<class 'str'>
int(hex(h),16) # 将十六进制的字符串转为十进制的整数 输出：10

# 2.7、oct() 将一个整数转换为八进制的字符串
j = 20
oct(j),type(oct(j)) # 输出：0o24  类型：<class 'str'>
int(oct(j),8) # 将八进制的字符串转为十进制的整数 输出：20

# 2.7、bin() 将一个整数转换为二进制的字符串
k = 30
bin(k),type(bin(k)) # 输出：0b11110 类型：<class 'str'>
int(bin(k),2) # 将八进制的字符串转为十进制的整数 输出：30

