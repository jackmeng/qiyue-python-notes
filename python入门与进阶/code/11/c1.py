from enum import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    red = 4


print(VIP.YELLOW)
print(type(VIP.YELLOW))
print(VIP.YELLOW.name)
print(type(VIP.YELLOW.name))
print(VIP['YELLOW'])
print(type(VIP['YELLOW']))
print(VIP['YELLOW'].name)
print(type(VIP['YELLOW'].name))

for v in VIP:
    print(v)
    print(v.name)