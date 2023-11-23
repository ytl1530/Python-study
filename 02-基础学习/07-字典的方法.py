"""
字典的方法：
    obj[key] = value 向字典中添加元素
    obj.keys()    获取字典中所有的key数据
    obj.values()  获取字典中所有的value数据
    obj.pop(key,default)  key存在获取相应的value,同时删除key-value对,否则获取默认值
    obj.popitem() 随机从字典中取出一个key-value对,结果为元组类型,同时将该key-value从字典中删除
    obj.clear()   清空字典中所有的key-value对
"""
# 创建字典
obj = {'name':'张三','age':18,'sex':'男'}

# 向字典中添加元素
obj['score'] = 98
print(obj)

# 获取字典中所有的key
key_vals = obj.keys()
print(key_vals)
print(list(key_vals))  # 转为列表
print(tuple(key_vals)) # 转为元组

# 获取字典中所有的value
value_vals = obj.values()
print(value_vals)
print(list(value_vals))  # 转为列表
print(tuple(value_vals)) # 转为元组

# 删除字典中的元素
pop_val = obj.pop('score') # 根据key值删除指定元素
print(pop_val)
print(obj)

pop_val1 = obj.popitem() # 随机删除元素
print(pop_val1)
print(obj)

# 清空字典中的数据
obj.clear()
print(obj)


"""
字典的生成式：
    obj = { key:value for item in range }
    obj = { key:value for key,value in zip(list1,list2) }
"""
import random

obj1 = {item:random.randint(1,100) for item in range(1,6)}
print(obj1)

lst1 = [1001,1002,1003]
lst2 = ['张三','李四','王五']
obj2 = {key:value for key,value in zip(lst1,lst2)}
print(obj2)

