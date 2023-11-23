# 序列的相关操作
"""
    x in s     ： 如果 x 是 s 的元素，结果为True，否则为False
    x not in s ： 如果 x 不是 s 的元素结果为True，否则为False
    len(x)     ： 序列 x 中的元素个数(即序列的长度)
    max(x)     ： 序列 x 中元素的最大值
    min(x)     ： 序列 x 中元素的最小值
    s.index(x) ： 序列 s 中第一次出现元素 x 的位置
    s.count(x) ： 序列 s 中出现 x 的总次数

"""
# 序列的相加和相乘操作
sr1 = 'hello'
sr2 = 'world'
print(sr1+sr2) # 相加
print(sr1*3)   # 相乘

# in 操作符的使用
print('e在sr1中存在吗',('e' in sr1)) # True
print('w在sr1中存在吗',('w' in sr1)) # Flase

# not in 操作符的使用
print('e在sr1中不存在吗',('e' not in sr1)) # Flase
print('w在sr1中不存在吗',('w' not in sr1)) # True

# 内置函数的使用
print(len(sr2)) # 5
print(max(sr2)) # w
print(min(sr2)) # d

# 序列对象方法的使用
print(sr2.index('l')) # 3
print(sr1.count('l')) # 2