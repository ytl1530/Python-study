"""
列表的基本方法：
    list.append(x)          在列表list最后添加 x 元素
    list.insert(index,x)    在列表list中index的位置前插入 x 元素
    list.clear()            清除列表list中的所有元素
    list.pop(index)         将列表list中的index位置的元素取出，并从列表中将其删除
    list.remove(x)          将列表list中出现的第一个元素 x 删除
    list.reverse()          将列表list中的元素反转
    list.copy()             复制list列表中的所有元素并生成一个新的列表
"""

lst = ['张三','李四','王五','周六','孙七','周八','吴九']
print(lst)

# 在列表的最后面添加一个元素
lst.append('郑十')
print(lst)  

# 在列表中插入一个元素
lst.insert(2,'lisi')
print(lst)

# 删除指定索引位置的值
lst.pop(1)
print(lst)

# 删除指定元素
lst.remove('lisi')
print(lst)

# 复制列表
lst1 = lst.copy()
print(lst1)

# 清除列表中的值
lst1.clear()
print(lst1)

# 反转列表
lst.reverse()
print(lst)

# 修改列表中的值
lst[1] = '李四'
print(lst)

"""
列表的排序：
    sort():           list.sort(key=None,reverse=False)
    内置函数sorted():  sorted(iterable,key=None,reverse=False) 
    key: 表示排列的规则; reverse: 表示排序方式(默认为升序); iterable: 表示排列的对象
"""

# 使用 sort 方法排序

# 整数排序
lst2 = [3,12,5,54,32,123]
print(lst2)

lst2.sort() # 升序
print(lst2)
lst2.sort(reverse=True) # 降序
print(lst2)

# 英文字符串排序
lst3 = ['hello','World','php','Python'] 
lst3.sort() # 升序：先排大写，后排小写
print(lst3)
lst3.sort(reverse=True) # 降序：先排小写，后排大写
print(lst3)

# 添加条件排序
lst3.sort(key=str.lower) # 将大写转小写排序
print(lst3)

# 使用内置函数 sorted 排序 产生一个新的列表,使用方法和sort基本一致，上面的操作 sorted 函数都可以操作
lst4 = sorted(lst2)
print(lst4)

"""
列表生成式：
    list = [expression for item in range]
    list = [expression for item in range if condition]
    expression: 列表中的元素
    condition: 条件语句
"""

import random

# 生成一个 1-10 的列表
lst5 = [item for item in range(1,11)]
print(lst5)

# 生成一个 1-100 中间的随机数个数为10的列表
lst6 = [random.randint(1,100) for item in range(1,11)]
print(lst6)

# 根据条件生成一个列表
lst7 = [item for item in range(1,21) if item%2==0]
print(lst7)

"""
二维列表生成式：
    list = [[expression for item in range] for item in range]
二维列表遍历：
    for row in list:
        for item in row:
            pass
"""
# 使用 [] 生成一个二维数组
lst8 = [
    ['姓名','年龄','性别'],
    ['张三',18,'男'],
    ['李四',20,'女'],
    ['王五',19,'女'],
]

# 使用生成式生成一个二维数组
lst9 = [[i for i in range(1,4)] for item in range(1,6)]

# 遍历二维数组
for row in lst8:
    for item in row:
        print(item,end='\t')
    print()





