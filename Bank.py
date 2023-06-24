money = 5000


def main():
    print('----------主菜单------------'
          '\n您好，欢迎来到ATM，请选择操作:')
    print('查询余额\t【输入1】'
          '\n存款\t\t【输入2】'
          '\n取款\t\t【输入3】'
          '\n退出\t\t【输入4】')
    return int(input('请输入您的操作：'))


def check():
    print('----------查询余额------------')
    print(f'您好，您的余额为：{money}元')


def put_in(num):
    global money
    money += num
    print('----------存款------------')
    print(f'存款{num}元成功')
    print(f'您的当前余额为：{money}元')


def put_out(num):
    global money
    money -= num
    print('----------取款------------')
    print(f'您的取款金额为：{num}元')
    print(f'您的当前余额为：{money}元')


while True:
    key_board = main()
    if key_board == 1:
        check()
        continue
    elif key_board == 2:
        num = int(input('请输入存款金额：'))
        put_in(num)
        continue
    elif key_board == 3:
        num = int(input('请输入取款金额：'))
        put_out(num)
        continue
    else:
        break

