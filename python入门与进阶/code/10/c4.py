import re

a = 'python1111C#java678php'

# 第三个参数 设置为 re.I 表示忽略大小写进行匹配
r = re.findall('c#',a,re.I)

print(r)

# 第三个参数 设置为 re.I 表示忽略大小写进行匹配
# re.S 表示让 . 可以匹配换行符, . 原本可以匹配的是除换行符之外的任意字符
# 使用 | 分开,  re.I 和 re.S 都生效, 还可以写更多的参数
r = re.findall('c#.',a,re.I | re.S)