# 匿名函数

def add(x,y):
    return x+y

print(add(1,2))

# lambda parameter_list: expression
f = lambda x,y: x+y

print(f(1,2))

# 三元表达式
# 条件为真时返回的结果 if 条件判断 else 条件为假时返回的结果
x=2
y=1

# 如果 x 大于 y , 则 返回 x,  否则 返回y
r = x if x > y else y

print(r)
