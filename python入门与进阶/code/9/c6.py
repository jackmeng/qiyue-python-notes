""" 
继承
"""
class Parent():
    name = ''
    age = 18
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def getInfo(self):
        return self.name,self.age
# 将父类写在括号中(支持多继承)
class Sub(Parent):
    school = '人民路小学'

    def __init__(self,name,age,school):
        self.school = school
        # 使用类名可以调用父类的方法, 不推荐这样使用
        Parent.__init__(self,name,age)
        # 推荐使用 super 的方式调用父类方法
        super(Sub,self).__init__(name,age)
        # Python3 中 super 可以不用传参数
        super().__init__(name,age)
    
    def getInfo(self):
        return self.school,Parent.getInfo(self)

sub = Sub('花仙子',16,'花园路小学')
print(sub.getInfo())