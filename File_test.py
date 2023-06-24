file = open('D:/bill.txt', 'r', encoding='UTF-8')
new_file = open('D:/bill.txt.bak', 'w', encoding='UTF-8')

for data in file:
    data = data.strip()
    if data.split('，')[-1] == '测试':
        continue
    else:
        new_file.write(data)
        new_file.write('\n')
file.close()
new_file.close()
