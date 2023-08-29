import utils.screenshot

# screenshot = utils.screenshot.capture_screenshot()

import keyboard
import pyautogui
import time
import os
import easyocr
import pyperclip

def on_triggered_hotkey():
    # 按下ctrl+alt+d
    time.sleep(0.1)

    print('shift+alt+o are pressed')

    screenshot = utils.screenshot.capture_screenshot()

    # %%

    reader = easyocr.Reader(['ch_sim', 'en'])  # this needs to run only once to load the model into memory
    result = reader.readtext('screenshot.png',detail=0)
    text=''.join(result)
    pyperclip.copy(text)
    print(''.join(result))







# 定义快捷键组合，例如 'ctrl+alt+a'
hotkey = 'shift+alt+o'

# 当快捷键被触发时，调用 on_triggered_hotkey 函数
keyboard.add_hotkey(hotkey, on_triggered_hotkey)

# 阻止程序退出，保持监听状态
keyboard.wait()