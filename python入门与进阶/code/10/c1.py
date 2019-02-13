import re

a = 'C|C++|Java|c#|Python|Javascript'

print(a.index('Python')>-1)

print('Python' in a)

r = re.findall('Python',a)
print(r)

if len(r) > 0:
    print('字符串包含Python')
else:
    print('No')