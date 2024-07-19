import tkinter as tk
import tkinter.messagebox
import os

cur_path = os.getcwd()
top = tk.Tk()
top.title("网易云ncm转换mp3/flac工具")
top.geometry("400x300")
top.resizable(0, 0)
tk.Label(top, text="本GUI基于github项目ncmdump制作\n网址：https://github.com/taurusxin/ncmdump").place(x=50, y=20)

# 请输入文件地址
tk.Label(top, text="请输入音乐文件夹地址：").place(x=50, y=60)
entry = tk.Entry(top, width=40)
entry.place(x=50, y=80)
# 请输入dumpncm的地址
tk.Label(top, text="请输入dumpncm.exe的地址：").place(x=50, y=110)
entry1 = tk.Entry(top, width=40)
entry1.place(x=50, y=140)
# 初始设置
entry1.insert(0, cur_path)


def convert():
    path = entry.get()
    dumpncm = entry1.get()
    #如果有错误，弹窗提示
    infomsg = ""
    isOK = 1
    if not os.path.exists(dumpncm+"/ncmdump.exe"):
        infomsg = "请正确输入ncmdump.exe的地址"
        isOK = 0
    if not os.path.exists(path):
        infomsg = infomsg + "\n请正确输入音乐文件夹地址"
        isOK = 0
    if isOK == 0:
        tkinter.messagebox.showinfo('提示', infomsg)
        return
    code = dumpncm + "/ncmdump.exe -d " + path
    result = os.system(code)
    if(result == 0):
        tkinter.messagebox.showinfo('提示', '转换成功\n文件已保存在' + path + '文件夹下')
    else:
        tkinter.messagebox.showinfo('提示', '转换失败')


# 转换按钮
w = tk.Button(top, text="开始转换", command=convert)
w.place(x=50, y=200)


top.mainloop()
