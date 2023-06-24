import json

data1 = [{'name': 'Jack', 'age': 21, 'gender': 'male'}, {'name': '汤姆', 'age': 20, 'gender': 'male'},
         {'name': 'Taylor', 'age': 31, 'gender': 'female'}]
json_str1 = json.dumps(data1, ensure_ascii=False)       # json.dumps(),将json格式转换为字符串
print(json_str1)
print(type(json_str1))

data2 = {'name': 'Jay Chou', 'addr': '中国台湾'}
json_str2 = json.dumps(data2, ensure_ascii=False)
print(json_str2)
print(type(json_str2))

my_str1 = '[{"name": "Jack", "age": 21, "gender": "male"}, {"name": "汤姆", "age": 20, "gender": "male"}, {"name": "Taylor", "age": 31, "gender": "female"}]'
new_data1 = json.loads(my_str1)         # json.loads(),将字符串转换成json格式(列表或字典)
print(new_data1)
print(type(new_data1))

my_str2 = '{"name": "Jay Chou", "addr": "中国台湾"}'
new_data2 = json.loads(my_str2)
print(new_data2)
print(type(new_data2))
