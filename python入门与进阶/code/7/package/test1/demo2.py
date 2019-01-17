import demo # 导入当前包下的模块
import sub.demo # 导入子包的module_name
import sub.demo2 as sd2 # 对导入的module取别名

print(demo.a)
print(sub.demo.a)
print(sd2.a)