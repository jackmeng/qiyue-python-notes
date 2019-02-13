# 定义两个函数
# 1.实现两个数字相加
# 2.打印输入的参数
import sys
sys.setrecursionlimit(10000) # 设置允许最大递归层数

def add(x,y):
    result = x + y
    return result

# def print(code):
#     print(code) # 函数内部调用自身叫做递归调用,这里会造成死循环,达到最大限制层级后程序停止 

# 定义函数 避免和内置函数重名

def print_code(code):
    print(code) 

a = add(1,2)
b = print_code('Python')
print(a)
print(type(b))
print(a,b)