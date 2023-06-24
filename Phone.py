# 变量或者方法前加 __ 表示私有属性或方法，外部不能够调用，仅供类内私有调用

class Phone:
    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable:
            print('5G开启')
        else:
            print('5G关闭，使用4G网络')

    def call_by_5g(self):
        self.__check_5g()
        print('正在通话中...')


phone = Phone()
phone.call_by_5g()
