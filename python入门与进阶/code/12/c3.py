# map

list_x = [1,2,3,4,5,6,7,8]

list_y = [1,2,3,4,5,6]

r1 = map(lambda x: x*x,list_x)
r2 = map(lambda x,y:x*x+y,list_x,list_y)

print(list(r1))
print(list(r2))