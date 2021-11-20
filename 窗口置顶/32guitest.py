#置顶Tk
import tkinter as tk
import win32gui as gui
import win32con as con
#获取所有窗口句柄
hwnd_title = {}
  
def get_all_hwnd(hwnd, mouse):
    if (gui.IsWindow(hwnd)
            and gui.IsWindowEnabled(hwnd)
            and gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: gui.GetWindowText(hwnd)})
  
#置顶窗口
print("Python置顶展台窗口 | 版本 2021.11.20-22471")
hwnd = gui.FindWindow(None, 'tk')
# hwnd = gui.FindWindow('xx.exe', None)
# 窗口需要正常大小且在后台，不能最小化
gui.ShowWindow(hwnd, con.SW_SHOWNORMAL)
# 窗口需要最大化且在后台，不能最小化
# ctypes.windll.user32.ShowWindow(hwnd, 3)
gui.SetWindowPos(hwnd, con.HWND_TOPMOST, 0, 0, 0, 0,
                              con.SWP_NOMOVE | con.SWP_NOACTIVATE | con.SWP_NOOWNERZORDER | con.SWP_SHOWWINDOW | con.SWP_NOSIZE)
#取消置顶
#gui.SetWindowPos(hwnd, con.HWND_NOTOPMOST, 0, 0, 0, 0,con.SWP_SHOWWINDOW|con.SWP_NOSIZE|con.SWP_NOMOVE)
  
if __name__ == '__main__':
    pass