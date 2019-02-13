# 函数的参数
""" 
1. 必须参数
2. 关键字参数
3. 默认参数
"""
# x和y 是必须参数, 调用时必须传入值, 否则会报错
def add(x,y): 
    pass
#这个函数有两个必须参数,调用只传入了一个参数,会报错
add(1) 
# 调用时可以使用 关键字参数,改变传入参数的顺序,提升可读性
add(y=1,x=3) 

def print_student_files(name,gender,age,college):
    print('我叫'+name)
    print('我今年'+str(age)+'岁')
    print('我是'+gender+'生')
    print('我在'+college+'上学')

# 调用 print_student_files 函数 需要每次都传入4个参数
# 将函数改造一下,加上默认参数

def print_student_files(name,gender='男',age=18,college='人民路小学'):
    print('我叫'+name)
    print('我今年'+str(age)+'岁')
    print('我是'+gender+'生')
    print('我在'+college+'上学')

# 可以使用以下方式调用
print_student_files('小明')
print_student_files('小红','女')
print_student_files('小强',age=19)
#不可以这样调用
print_student_files('小刚',gender='男',17)

# 不可以在默认参数后面跟必须参数,这样会报错
def test(a='abc',b):
    pass