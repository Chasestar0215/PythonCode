import os

# os.system('cmd.exe')        # 调用os.system()直接打开“系统文件”
os.startfile("D:\\LenovoSoftstore\\Install\\kugouyinle\\KuGou.exe")         # 调用os.startfile()直接打开“可执行文件”

# os模块的常用方法
'''
os.getcwd()                                 # 返回当前的工作目录
os.listdir('path')                          # 返回指定路径下的文件和目录信息
os.mkdir('path',mode='')                    # 创建目录
os.makedirs('path1/2/...',mode='')          # 创建多级目录
os.rmdir('path')                            # 删除目录
os.removedirs('path1/2/...')                # 删除多级目录
os.chdir('path')                            # 将path设置为当前工作目录
'''