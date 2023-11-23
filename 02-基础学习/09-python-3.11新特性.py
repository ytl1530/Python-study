"""
1、结构模型匹配
    match data:
        case {}:
            pass
        case []:
            pass
        case ():
            pass
        case _:
            pass
2、字典合并运算符
   字典3 = 字典1 | 字典2
3、同步迭代
    match data1,data2:
        case data1,data2:
            pass
"""
# 模式匹配
score = input('请输入用户成绩：')
match score:
    case 'A':
        print('还行')
    case 'B':
        print('不行')
    case 'C':
        print('差劲')
    case 'D':
        print('垃圾')

# 字典合并运算符
obj1 = {10:'张三',20:'李四'}
obj2 = {30:'王五',40:'周六'}
obj3 = obj1 | obj2
print(obj3)

# 同步迭代
data1 = [1,2,3,4,5]
data2 = [6,7,8,9,0]
match data1,data2:
        case 1,7:
            print('匹配')

