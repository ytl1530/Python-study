# eval()：内置函数，主要作用是去掉字符串两边的引号,相当于将字符串隐式的转换了类型
# eval() 经常和 input() 一起使用
# 主要语法：变量 = eval(字符串)

a = '3.14'
eval(a) # 输出：3.14 类型：<class 'float'>

b = eval(input('请输入年龄：')) # 输出：18  类型：<class 'int'>

