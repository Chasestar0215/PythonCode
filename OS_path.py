import os.path

print(os.path.abspath('OS.py'))             # os.path.abspath('path')获取文件或目录的绝对路径
print(os.path.exists('KuGou.exe'))          # os.path.exists('path')判断文件或目录是否存在
print(os.path.join('C:\\', 'OS.py'))        # os.path.join('path1','path2')拼接路径
print(os.path.split(r'C:\Users\逐星i\OneDrive\桌面\PythonCode\PycharmProjects\pythonProject\My_project\Learn\OS.py'))   # os.path.split('path')将路径与文件拆分
print(os.path.splitext('OS.py'))            # os.path.splitext('path')将文件名与扩展名拆分

'''
os.path.basename('path')从一个目录中提取文件名
os.path.dirname('path')从一个目录中提取目录，不包括文件名
os.path.isdir('path')判断是否为路径而非文件
'''
