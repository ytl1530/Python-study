# 序列：用于存储多个值的连续空间，每个值都对应一个整数的编号，称为 索引

"""
索引
    正向递增索引
    逆向递减索引
"""
# 正向递增索引
sr = 'helloworld'
for i in range(0,len(sr)):
    print('索引：',i,'对应的字符：',sr[i])

# 逆向递减索引
sr = 'helloworld'
for i in range(-len(sr),0):
    print('索引：',i,'对应的字符：',sr[i])

# 序列的切片操作：序列[开始位置,结束位置,步长]
sr = 'helloworld'
print(sr[0:5:2])
print(sr[:5:2])  # 省略开始位置 默认开始位置是 0
print(sr[:5])    # 省略开始位置和步长 默认步长为 1
print(sr[0::2])  # 省略结束位置 默认到最后一个字符结束(包含最后一个字符)
print(sr[5::])   # 省略结束位置和步长
print(sr[5:])    # 省略结束位置和步长
print(sr[::1])   # 将字符串中的所有字符正序输出
print(sr[::-1])  # 将字符串中的所有字符逆序输出