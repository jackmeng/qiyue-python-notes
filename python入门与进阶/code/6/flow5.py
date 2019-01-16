'''
if 可以独立使用  else 不可以
pass 空语句, 占位语句 
'''

# if 是可以像下面这样嵌套的
# if condition:
#     if condition:
#         pass
#     else:
#         pass
#     pass
# else:
#     if condition:
#         pass
#     else:
#         pass
#     pass

a = input()
print('a is ' + a)
a = int(a) # 接收到的用户输入是 str 类型, 所以要转成 int 才可以进行下面的判断
if a == 1:
    print('apple')
elif a == 2:
    print('orange')
else :
    print('other')
'''
python 中没有 switch 关键字,
1. 可以利用elif 实现 switch 功能
2. 可以利用字典实现 switch 功能
'''

a = 1
b = 0
# a 和 b 中有一个为真 ,  获取其中为真的数据
# 可以用if  else 
# 更简洁的方式是   a or b