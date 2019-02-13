class Student():
    sum = 0
    name = '' 
    age = 0 
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__class__.sum += 1
        print('当前班级学生总数:'+str(self.__class__.sum))
    def do_homework(self):
        print('name:' + self.name)
        print('age:' + str(self.age))

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

    @staticmethod
    def add(x,y):
        pass

student1 = Student('石敢当',18)

