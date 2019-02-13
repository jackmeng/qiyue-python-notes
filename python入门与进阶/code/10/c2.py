import re

a = 'C0C++7Java8c#6Python1Javascript'

# \d 元字符 表示 数字
r = re.findall('\d',a)
print(r)
r = re.findall('\D',a)
print(r)