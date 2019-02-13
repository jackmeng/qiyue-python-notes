import re

lanuage = 'PythonC#JavaC#PHPC#'

def convert(value):
    print(value.group())
    matched = value.group()
    return '!!!'+matched+'!!!'


r= re.sub('C#', convert, lanuage)
# re.match() 从头开始匹配, 不符合, 就不继续
# re.search() 匹配到即返回, 不继续匹配
print(r)