

import openai
import pyperclip
import time
import keyboard
openai.api_key = "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"

#
def on_triggered_hotkey():
    time.sleep(0.5)
    keyboard.send('ctrl+c')

    time.sleep(0.2)
    text=pyperclip.paste()
    time.sleep(0.2)
    print(text)
    # 访问GPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            # {"role": "system", "content": "用猫娘语气简要说明"},
            {"role": "user", "content": f"[{text}]. Help me modify the above keywords. Response format: 'keyword1_keyword2'. "},

        ]
    )
    print(response.choices[0].message.content)
    pyperclip.copy(response.choices[0].message.content)
    keyboard.send('ctrl+v')

# 定义快捷键组合，例如 'ctrl+alt+a'variable_name
hotkey = 'shift+alt+v'

# 当快捷键被触发时，调用 on_triggered_hotkey 函数
keyboard.add_hotkey(hotkey, on_triggered_hotkey)

# 阻止程序退出，保持监听状态:variable_name
keyboard.wait()

