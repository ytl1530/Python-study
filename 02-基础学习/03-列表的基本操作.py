"""
    列表：
    一系列按照特定顺序排列的元素组成
    是python中内置的可变序列
    在python中使用 [] 定义列表，元素与元素之间用英文逗号分开
    使用内置函数 list() 创建列表
    列表中的元素可以是任意数据类型
"""
# 创建与删除列表

# 1、使用 [] 创建列表
lst = ['hello','world',99,100.3,False]
# print(lst)

# 2、使用内置函数 list() 创建列表
lst2 = list('helloWorld')
# print(lst2)

# 3、删除整个列表
lst3 = [1,2,3]
del lst3 

# 4、列表的遍历操作

# 4.1、for 循环
lst4 = ['张三','李四','王五','周六']
for item in lst4:
    # print(item)
    pass

# 4.2、for 循环 + range函数 + len函数 根据索引获取列表中的元素
for i in range(0,len(lst4)):
    # print('索引：',i)
    # print('值：',lst4[i])
    pass

# 4.3、for 循环 + enumerate(列表,序号起始值)函数
for index,item in enumerate(lst4):
    # print(item,index) # index 是列表值的序号不是索引
    pass

for index,item in enumerate(lst4,1): # 修改index的起始值
    print(item,index) 
    pass


