counter = 1
while counter <= 10:
    counter += 1
    print(counter)
else: # 此处是在 while 循环完之后调用, 不是必须的
    print('EOF')

a = ['apple','orange','banana','grape']
for x in a:
    print(x)
# 嵌套
a = [['apple','orange','banana','grape'],(1,2,3)]
for x in a:
    for y in x:
        print(y,end='') # end='' 设置打印完成后面的字符,默认是换行
else: # else 是在循环遍历完成后调用 不是必须的
    print('loop end') 

a = [1,2,3]
for x in a:
    if x == 2:
        break # 跳出循环 跳出后不会执行else
    print(x)

for x in a:
    if x == 2:
        continue # 跳过本次循环 进行下一次循环 不影响 else 执行
    print(x)

for x in range(0,10):
    print(x,end=' | ') 
# 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
""" 
for(i=0;i<10;i++){
    print(x)
}
"""

for x in range(0,10,2):
    print(x,end=' | ') 
# 0 | 2 | 4 | 6 | 8 |
for x in range(10,0,-2):
    print(x,end=' | ') 
# 10 | 8 | 6 | 4 | 2 |

# 取出list中的 1 3 5 7
a = [1,2,3,4,5,6,7,8]
for i in range(0,len(a),2):
    print(a[i],end=' | ')
# 1 | 3 | 5 | 7 |
b = a[0:len(a):2]
print(b) # [1, 3, 5, 7]