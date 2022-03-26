# -*- coding:utf8 -*-
import os
#import send2trash

def del_files(path, end_name):
    for root, dirs, files in os.walk(path): #不要删这个看似没用的dirs
        for name in files:
            if name.endswith(end_name):  # 指定后缀
                os.remove(os.path.join(root, name))
                print("已删除文件: " + os.path.join(root, name)) #报告已删除的文件

def continue_or_not():
    go_on = input("请问还要继续嘛？输入n取消")
    if go_on == 'n':
        return False

if __name__ == "__main__":
    while (True):
        try:
            path = input("请粘贴要进行操作的文件夹路径：")
            #print(path)
            end_name = input("请输入要删除文件的文件名后方字符串共同点：")
            determination = input("确定？文件不会放入回收站！确认请输入y,输入n取消：")
            if determination == "y":
                del_files(path, end_name)
                print("ok")
                if continue_or_not() is False:
                    break
                else:
                    continue
            elif determination == "n":
                print("已取消")
                if continue_or_not() is False:
                    break
                else:
                    continue
            else:
                print("输入错误")
        except:
            print("程序出错！！")
    
    print('Bye!')
    os.system("pause") #没任何用处的暂停

# code by RepentStar
