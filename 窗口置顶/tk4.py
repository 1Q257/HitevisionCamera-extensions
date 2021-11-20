#Tkinter显示
import tkinter as tk
from tkinter import Widget, messagebox
import os
print("鸿合展台第三方控件 | 版本 2021.11.20-22504")
print("Powered By 老班长")
print('https://gitee.com/liubanlaobanzhang/')
tk2=tk.Tk()
img1=tk.PhotoImage(file='D:\LOGO\展台logo.png')
path1="C:/Users/Public/Desktop/鸿合视频展台.lnk"

def callback():
    os.startfile(path1)


button1 = tk.Button(tk2,image=img1,command=callback,text='站台',font='仿宋')
button1.pack()
tk2.geometry("128x128")
tk2.mainloop()