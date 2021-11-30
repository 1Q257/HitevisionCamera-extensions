#DEMO
#---MAIN-CODE---
#预加载 & 变量预设 & TK声明
import tkinter as tk
import os
print("鸿合展台第三方控件 | 版本 2021.11.20-22504")
print("Powered By 老班长")
print('https://gitee.com/liubanlaobanzhang/')
path1="C:/Program Files (x86)/HiClass/HiteCamera/HiteCameraShell/HiteCameraShell.exe"
tk2 = tk.Tk()
def callback():
    os.startfile(path1)
img1=tk.PhotoImage(file='D:\LOGO\展台logo.png')
button1 = tk.Button(tk2,image=img1,command=callback)
button1.pack()


class DragWindow:
    def __init__(self):
        tk2.x, tk2.y = 0, 0
        self.window_size = '128x64'

        # 设置隐藏窗口标题栏和任务栏图标
        tk2.overrideredirect(True)
        # 窗口透明度80%
        tk2.attributes("-alpha", 0.2)
        # 设置窗口大小、位置 长x宽+x+y
        tk2.geometry(f"{self.window_size}+1700+900")
        # 设定背景颜色
        tk2.configure(bg="blue")

        # 窗口移动事件
        tk2.bind("<B1-Motion>", self.move)
        # 单击事件
        tk2.bind("<Button-1>", self.get_point)
        # 双击事件
        tk2.bind("<Triple-Button-1>", self.close)

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


if __name__ == "__main__":
    window = DragWindow()
    window.run()

# pip install pyinstaller
# https://blog.csdn.net/lynjan/article/details/81557215