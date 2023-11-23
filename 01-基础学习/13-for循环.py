# 1、for 循环变量 in 遍历对象:

name = 'python' # 遍历字符串
for n in name:
    print('遍历的值：',n) 

# range(m,n) python中的内置函数，可创建一个整数列表，一般用在 for 循环中，函数中的 m 和 n，其中包含 m，但不包含 n，
arr = range(1,10)
for i in arr:
    print(i)

#求 100-999 之间的水仙花数，水仙花数为：abc = a*a*a + b*b*b + c*c*c

for i in range(100,1000):
    unit = i%10         # 个位
    decade = i//10%10   # 十位
    hundreds = i// 100  # 百位
    narcissus = unit ** 3 + decade ** 3 + hundreds ** 3
    if narcissus == i:
        print(i)

'''
2、for 循环变量 in 遍历对象: 
        语句块1 
    else: 
        语句块2
''' 
sum = 0
for i in range(1,11):
    sum+=i
else:
    print('1到20之间的累加和：',sum)
