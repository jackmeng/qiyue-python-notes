def damage(skill1,skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1, damage2 # 这样是返回一个元组(tuple)

damages = damage(3,6)
# damages是个元组(9,22)

skill1_damage, skill2_damage = damage(3,6)
# 这样会把返回值分别赋值给这两个变量,这样有利于下文使用,意义明确
# 这种接收方式在python中叫做序列解包
