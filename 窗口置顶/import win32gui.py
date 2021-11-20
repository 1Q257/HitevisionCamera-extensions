import win32gui
import win32con
#获取所有窗口句柄
hwnd_title = {}
  
def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd)
            and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
  
  
win32gui.EnumWindows(get_all_hwnd, 0)
for h, t in hwnd_title.items():
    if t :
        print (h, t)
#置顶窗口
print("置顶窗口")
hwnd = win32gui.FindWindow(None, "学习通答题助手")
# hwnd = win32gui.FindWindow('xx.exe', None)
# 窗口需要正常大小且在后台，不能最小化
win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
# 窗口需要最大化且在后台，不能最小化
# ctypes.windll.user32.ShowWindow(hwnd, 3)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)
#取消置顶
#win32gui.SetWindowPos(hwnd, win32.HWND_NOTOPMOST, 0, 0, 0, 0,win32con.SWP_SHOWWINDOW|win32con.SWP_NOSIZE|win32con.SWP_NOMOVE)
  
if __name__ == '__main__':
    pass