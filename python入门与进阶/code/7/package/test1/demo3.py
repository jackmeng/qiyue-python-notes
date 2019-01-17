from sub.demo import a
from sub import demo2
from sub.demo3 import * # 不推荐,引入不够明确
from sub.demo4 import *
from sub.demo4 import m2
# from sub.demo3 import m1,m2,m3 引入多个变量
""" 
from sub.demo3 import m1,m2,\
    m3
from sub.demo3 import (m1,m2,
    m3)
"""
print(a)
print(demo2.a)
print(path)
print(test)

print(m1)
print(m2)
print(m3)