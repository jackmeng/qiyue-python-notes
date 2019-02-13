class Student():
    name = '' # 称作 数据成员
    age = 0 
    # 必须定义第一个参数, 否则调用时报错
    # 推荐命名为 self  也可以自定义 如 this 等
    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))


# student = Student() # 实例化
# student.print_file()