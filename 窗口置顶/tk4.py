#Tkinter显示
import tkinter as tk
from tkinter import Widget, messagebox
import os
print("鸿合展台第三方控件 | 版本 2021.11.20-22504")
print("Powered By 老班长")
print('https://gitee.com/liubanlaobanzhang/')
tk2=tk.Tk(className='666')




class DragWindow:
    def __init__(self):
        # 窗口透明度80%
        tk2.attributes("-alpha", 0.2)
        tk2.x, tk2.y = 0, 0
        self.window_size = '300x200'

        tk2.overrideredirect(True)
        tk2.attributes("-alpha", 0.4)

        tk2.geometry(f"{self.window_size}+10+10")
        # 设定背景颜色
        tk2.configure(bg="blue")

        # 窗口移动事件
        tk2.bind("<B1-Motion>", self.move)

        def move(self, event):
            """窗口移动事件"""
            new_x = (event.x - tk2.x) + tk2.winfo_x()
            new_y = (event.y - tk2.y) + tk2.winfo_y()
            s = f"{self.window_size}+{new_x}+{new_y}"
            tk2.geometry(s)

        def get_point(self, event):
            """获取当前窗口位置并保存"""
            tk2.x, tk2.y = event.x, event.y

        def run(self):
            tk2.mainloop()

    def close(self, event):
        tk2.destroy()

window = DragWindow()
window.run()

tk2.geometry("256x128")
tk2.mainloop()
