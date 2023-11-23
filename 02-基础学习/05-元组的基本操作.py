"""
元组：
    是python中内置的不可变序列
    在python中使用 () 定义元组, 元素与元素之间使用英文逗号分隔
    元组中只有一个元素的时候, 逗号也不能省略
"""

"""
创建元组：
    1.直接使用 () 创建元组：元组名 = (item1,item2,...,itemN)
    2.使用内置函数 tuple() 创建元组：元组名 = tuple(序列)
删除元组
    del 元组名
"""

# 使用 () 创建元组
tup = ('张三',[1,2,3],99.9)
print(tup)

# 使用内置函数 tuple() 创建元组
tup1 = tuple('hello')
tup2 = tuple([100,99,98,97])
print(tup1)
print(tup2)

"""
    元组的遍历和列表的遍历是完全相同的
元组的生成式
    tuple = tuple((expression for item in range))
"""

# 元组生成式
tup3 = tuple((item for item in range(1,4)))
print(tup3)

# __next__取出元组生成式中的元素(取出的元素不会出在元组中)
tup4 = (item for item in range(1,4))
print(tup4.__next__())
print(tuple(tup4))



