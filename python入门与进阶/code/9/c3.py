class Student():
    name = '' 
    age = 0 
    # 构造函数的必须参数再实例化对象时必须传入
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # 在类的方法内通过 self.__class__ 可以放问当前类, 注意不是当前对象
        self.__class__.name

    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))


student1 = Student('石敢当',18)
student1.print_file()
# 对象的所有 数据成员
student1.__dict__ 

# 类也可以使用 __dict__
Student.__dict__