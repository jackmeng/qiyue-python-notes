'''
文件头要有说明
如:一段小程序,按照pylint规范修改代码
'''
# python 中没有常量(constant), pylint约定用 全部大写来定义常量
ACCOUNT = 'account'
PASSWORD = '123456'

# pylint 检测 认为 不在函数和类中的变量 就是常量,常量应当大写
print('请输入账号:')
USER_ACCOUNT = input() 
print('请输入密码:')
USER_PASSWORD = input()

if USER_ACCOUNT == ACCOUNT and USER_PASSWORD == PASSWORD:
    print('登录成功')
else:
    print('登录失败:账号或密码错误')