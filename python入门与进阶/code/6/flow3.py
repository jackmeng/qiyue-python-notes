# 模拟用户登录
# 假设正确的账号密码如下
account = 'account'  # 用户的账号
password = '123456'  # 用户的密码

print('请输入账号:')
# python 建议用下划线分割单词
user_account = input() # input() 接收用户输入
print('请输入密码:')
user_password = input()

if user_account == account and user_password == password :
    print('登录成功')
else:
    print('登录失败:账号或密码错误')
    