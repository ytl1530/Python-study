"""
集合
    python中的集合与数学中集合的概念一致
    python中的集合是一个无序不重复元素序列
    集合中只能存储不可变数据类型
    在python中集合使用 {} 定义
    与列表、字典一样,都是python中的可变数据类型
"""

"""
集合的创建：
    1.使用 {} 直接创建集合: s = {value1,value2,....}
    2.使用内置函数 set() 创建集合: s = set(迭代对象)
删除：
    del 集合名
"""

"""
集合的基本方法
    add()	                为集合添加元素
    clear()	                移除集合中的所有元素
    copy()	                拷贝一个集合
    difference()	        返回多个集合的差集
    difference_update()	    移除集合中的元素，该元素在指定的集合也存在。
    discard()	            删除集合中指定的元素
    intersection()	        返回集合的交集
    intersection_update()	返回集合的交集。
    isdisjoint()	        判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
    issubset()	            判断指定集合是否为该方法参数集合的子集。
    issuperset()	        判断该方法的参数集合是否为指定集合的子集
    pop()	                随机移除元素
    remove()	            移除指定元素
    symmetric_difference()	返回两个集合中不重复的元素集合。
    symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
    union()	                返回两个集合的并集
    update()	            给集合添加元素
    len()	                计算集合元素个数
"""

"""
集合的操作符
    A&B 交集
    A|B 并集
    A-B 差集
    A^B 补集
"""
