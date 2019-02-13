import re

s = 'abc, acc, adc, aec, afc, ahc'

# 匹配 a开头 中间是c或者f  最后是c 的字符
r= re.findall('a[cf]c',s)
print(r)
# 匹配 a开头 中间不是c或者f  最后是c 的字符
r= re.findall('a[^cf]c',s)
print(r)

# 匹配 a开头 中间是cdef中的一个  最后是c 的字符
r= re.findall('a[c-f]c',s)
print(r)