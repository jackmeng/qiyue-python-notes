class Student():
    sum = 0
    name = '' 
    age = 0 
    # 构造函数的必须参数再实例化对象时必须传入
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # 在类的方法内通过 self.__class__ 可以放问当前类, 注意不是当前对象
        self.__class__.sum += 1
        print('当前班级学生总数:'+str(self.__class__.sum))
    # 实例方法
    def do_homework(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

    # 类方法 使用 @classmethod 装饰,第一个参数约定为cls,代表当前类, 也可以是别的名字
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

     # 静态方法 使用 @staticmethod 装饰 没有约定参数  
    @staticmethod
    def add(x,y):
        pass


student1 = Student('石敢当',18)
# 可以使用对象调用类方法, 但是不建议这么去做
student1.plus_sum()
# Student.plus_sum()
# student2 = Student('喜小乐',18)
# Student.plus_sum()
# student3 = Student('小诺',18)
# Student.plus_sum()
