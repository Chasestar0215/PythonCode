t = float(input('请输入您的体温：'))


def check(temp):
    if 35 <= temp <= 37.3:
        print(f'您的体温是{temp}度,体温正常。')
    elif temp < 35:
        print('体温不在合理范围内！')
    else:
        print(f'您的体温是{temp}度，体温异常！')


check(t)
