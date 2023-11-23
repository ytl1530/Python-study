"""
字典类型：
    根据一个信息查找另一个信息的方式构成了 键值对 , 它表示索引用的键和对应的值构成成对的关系
"""

"""
创建字典：
    直接使用 {} 来创建字典: 字典名 = {key1:value,key2:value2...}
    通过内置函数 dict() 来创建字典: 字典名 = dict(key1=value1,key2=value2....)
    通过映射函数创建字典: 字典名 = dict(zip(list1,list2)) list可以是列表,也可以是元组
删除字典：
    del 字典名
"""

# 通过 {} 创建字典
obj1 = {'cat':10,'dog':20,'zoo':30}
print(obj1) 

# 通过内置函数 dict() 创建字典
obj2 = dict(cat=30,dog=20,zoo=10)
print(obj2)

# 通过映射函数 zip 创建字典
lst1 = ['zoo','cat','dog']
lst2 = [100,200,300]
obj3 = dict(zip(lst1,lst2))
print(obj3)

# 删除字典
del obj1

"""
字典元素的取值：
    obj[key] 或 obj.get(key)
    使用 obj[key] 的时候当 key 不存在时 会报错
    使用 obj.get(key) 的时候当 key 不存在时 可以设置默认值
字典元素的遍历：
    1.遍历出key与value的元组
        for item in obj.items()
            pass
    2.分别遍历出key和value
        for key,value in obj.items()
            pass
"""
# 使用 obj[key] 获取字典中的值
print(obj2['cat'])

# 使用 obj.get(key) 获取字典中的值
print(obj2.get('zoo'))

# 当 key 不存在时 使用 obj.get(key) 设置默认值, 并不会在字典中添加一个元素
print(obj2.get('panda',100))
print(obj2)

