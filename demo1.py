str1 = 'Jack'
str2 = 'Python'
str3 = 'Java'


def length(string):
    count = 0
    for _ in string:
        count += 1
    print(string + '字符串长度为：', count)


if __name__ == '__main__':      # 只有独自运行该模块才会执行，其他模块调用不执行
    length(str1)
    length(str2)
    length(str3)
