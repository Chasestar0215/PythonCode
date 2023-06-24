file = open('D:/word.txt', 'r')
data = file.read()
itheima = data.split()
flag = 0
for i in itheima:
    if i == 'itheima':
        flag += 1

print(f'word.txt文件中存在{flag}个itheima')
file.close()
