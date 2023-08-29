import keyboard
import pyautogui
import time
import os

def on_triggered_hotkey():
    # 按下ctrl+alt+d
    time.sleep(0.1)

    print('shift+alt+o are pressed')

    wechat_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\微信\微信.lnk'
    os.startfile(wechat_path)




# 定义快捷键组合，例如 'ctrl+alt+a'
hotkey = 'shift+alt+o'

# 当快捷键被触发时，调用 on_triggered_hotkey 函数
keyboard.add_hotkey(hotkey, on_triggered_hotkey)

# 阻止程序退出，保持监听状态
keyboard.wait()