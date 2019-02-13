import json

json_str = '{"name":"qiyue","age":18}'

student = json.loads(json_str)
print(student)
print(type(student))

json_str = '[{"name":"qiyue","age":18,"flag":false},{"name":"xiaoming","age":16}]'

student = json.loads(json_str)
print(student)
print(type(student))

student = [
        {"name":"qiyue","age":18,"flag":False},
        {"name":"xiaoming","age":16}
    ]

json_str = json.dumps(student)
print(json_str)
print(type(json_str))