import tkinter
from tkinter import ttk
 
 
def xFunc1(event):
    print(f"特殊按键触发:{event.char},对应的ASCII码:{event.keycode}")
 
 
win = tkinter.Tk()
win.title("Kahn Software v1")    # #窗口标题
win.geometry("600x500+200+20")   # #窗口位置500后面是字母x
'''
响应特殊按键事件
<Shift_L>     左shift按键响应
<Shift_R>     右shift按键响应
<F2>          F2按键相应，F3,F4.....
<Return>      回车按键相应
<BackSpace>   退格删除键相应
a    指定按键盘a键触发
x    指定按键盘x键触发
'''
 
win.bind("<Triple-F2>", xFunc1)
# win.bind("a", xFunc1)
# win.bind("x", xFunc1)
 
win.mainloop() 