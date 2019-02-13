import re

lanuage = 'PythonC#\nJavaPHP'
# 替换字符串
r= re.sub('C#', 'GO', lanuage)
print(r)

lanuage = 'PythonC#JavaC#PHPC#'

r= re.sub('C#', 'GO', lanuage,2)
print(r)

lanuage = lanuage.replace('C#', 'GO')

print(lanuage) # PythonGOJavaGOPHPGO