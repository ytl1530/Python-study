# continue 跳过本次循环，后续循环继续执行，通常与 if 语句搭配使用

# 在 while 中使用：求 1-100 之间的偶数和
s = 0
i = 1
while i<=100:
    if i%2==1:
        i+=1
        continue
    s+=i
    i+=1
print('1-100 之间的偶数和:',s)


# 在 for 中使用：求 1-100 之间的奇数和
m=0
for n in range(1,101):
    if n%2==0:
        continue
    m+=n
print('1-100 之间的奇数和:',m)
    

