# 1、"千年虫"是什么虫; 需求：已知一个列表中存储的是员工的出生年份[88,89,90,98,00,99],由于时间较久，出生的年份均为2位整数，现需要2位年份前添加19，如果年份是00，将需要加上200
year_list = [88,89,90,98,00,99]
for index,item in enumerate(year_list):
    if item != 0:
        year_list[index] = '19' +  str(item)
    else:
        year_list[index] = '200' + str(item)
print(year_list)

"""
    2、 模拟京东购物流程；需求：从键盘录入5个商品信息（1001 手机）添加到商品列表中，展示商品信息，
    提示用户选择商品，用户选中的商品添加到购物车中（购物车中的商品要逆序的），
    用户选中的商品不存在时需要有相应的提示，当用户输入q时循环结束，显示购物车中的商品
    1001 手机
    1002 电脑
    1003 笔记本
    1004 显示屏
    1005 鼠标
"""
# goods_list = []

# for item in range(1,6):
#     good = input('请输入商品编号和名称: ')
#     goods_list.append(good)

# for good in goods_list:
#     print(good)

# goods_cart = []

# while len(goods_list):
#     flag = False
#     cart = input('请选择需要购买的商品或者输入q退出购物车: ')
#     for index,good in enumerate(goods_list):
#         if cart == good[0:4]:
#             goods_cart.append(goods_list.pop(index))
#             print('添加购物车成功！')
#             flag = True
#             break

#     if flag == False and cart != 'q':
#         print('商品不存在')

#     if cart == 'q':
#         goods_cart.reverse()
#         for car in goods_cart:
#             print(car)
#         break
# else:
#     goods_cart.reverse()
#     for car in goods_cart:
#         print(car)
#     print('商品已经全部加入购物车！')

# 3、模拟12306火车票订票流程; 需求：假设北京到天津有以下四个车次可供选择，用户选择所要购买的车次，进行购票进站
train_head = ['车次','起始站','发车时间','到达时间','所需时长']
train_number={
    'G1569':['北京南-天津南','18:06','18:39','00:33'],
    'G1567':['北京南-天津南','18:15','18:49','00:34'],
    'G8917':['北京南-天津西','18:20','19:19','00:59'],
    'G203':['北京南-天津南','18:35','19:09','00:34']
}
# for head in train_head:
#     print(head,end='   ')
# print()
# for key in train_number.keys():
#     print(key,end='  ')
#     for val in train_number[key]:
#         print(val,end='  ')
#     print()

# while True:
#     train = input('请选择需要购买的车次:')
#     flag=False
#     tarin_key = ''
#     user = ''
#     for key in train_number.keys():
#         if key == train:
#             user = input('请输入需要购买车票的用户姓名: ')
#             tarin_key = key
#             flag=True
#             break

#     if flag == False:
#         print('暂无该车次')
#     else:
#         print('您已购买了',tarin_key,train_number[tarin_key][0],train_number[tarin_key][1],'开,请',user,'尽快换取纸质车票----【铁路客服】')
#         user=''
#         break       

# 4、模拟手机通讯录; 需求：从键盘中录入5位好友的姓名和电话，由于通讯录是无序的所以可以使用集合来实现
# phone_book = set()

# for i in range(0,5):
#     phone = input('请输入好友姓名和电话:')
#     phone_book.add(phone)

# for item in phone_book:
#     print(item)

# 温度计1
# temperature = input()
# if temperature[-1] == 'C' or temperature[-1] == 'c' :
#     F = float(temperature[:-1]) * 1.8 + 32
#     if str(round(F,2))[-1] == '0':
#         print(str(round(F,2))+'0F')
#     else: 
#         print(str(round(F,2))+'F')
# elif temperature[-1] == 'F' or temperature[-1] == 'f' :
#     C = (float(temperature[:-1]) - 32 ) / 1.8
#     if str(round(C,2))[-1] == '0':
#         print(str(round(C,2))+'0C')
#     else:
#        print(str(round(C,2))+'C') 
# else:
#     print('输入格式错误')

# 将输入的数字转为中文数字
# template = "零一二三四五六七八九"

# num = input()
# for i in num:
#     print(template[eval(i)], end="")

# 温度计2
temperature = input()

if temperature[0] == 'C' or temperature[0] == 'c' :
    F = float(temperature[1:]) * 1.8 + 32
    if str(round(F,2))[-1] == '0':
        print('F'+str(round(F,2))+'0')
    else: 
        print('F'+str(round(F,2)))
elif temperature[0] == 'F' or temperature[0] == 'f' :
    C = (float(temperature[1:]) - 32 ) / 1.8
    if str(round(C,2))[-1] == '0':
        print('C'+str(round(C,2))+'0')
    else:
       print('C'+str(round(C,2))) 
else:
    print('输入格式错误')


            
    
