# 通过import 导入的时候会自动调用这个文件
# 可以使用 __init__ = ['module_name'] 限制 使用 from package_name import * 导入包时导入的模块
""" 
import sys
import datetime
import io
可以在 __init__.py 引入公共模块
然后在需要的文件 import package_name
使用时 package_name.sys
"""

# 包和模块是不会被重复导入的
# 避免循环导入