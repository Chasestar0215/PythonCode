def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, 'r', encoding='UTF-8')
        print(f'读取的文件数据是:\n{f.read()}')
    except BaseException as e:
        print(f'异常是：{e}')
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    f = open(file_name, 'a', encoding='UTF-8')
    f.write(data)
    f.close()


if __name__ == '__main__':
    print_file_info('D:/bill.txt')
    append_to_file('D:/bill.txt', '这是测试。')
