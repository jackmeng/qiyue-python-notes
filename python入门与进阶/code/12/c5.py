# filter

list_x = [1,0,1,0,0,1]

r = filter(lambda x: True if x == 1 else False, list_x)
r = filter(lambda x: x, list_x) # 与上面的返回结果一致
print(list(r))