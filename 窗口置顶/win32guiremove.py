#重置窗口置顶
import win32gui
import win32con
import os
hwnd = win32gui.FindWindow(None, 'tk')
win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,win32con.SWP_SHOWWINDOW|win32con.SWP_NOSIZE|win32con.SWP_NOMOVE)
os.system('taskkill python.exe')