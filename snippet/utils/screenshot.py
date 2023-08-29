import tkinter as tk
import pyautogui
from PIL import Image, ImageTk

def capture_screenshot():
    def on_click(event):
        nonlocal start_x, start_y
        start_x = event.x
        start_y = event.y
        canvas.create_rectangle(start_x, start_y, start_x, start_y, outline='red', tag='line')

    def on_drag(event):
        canvas.delete('line')
        canvas.create_rectangle(start_x, start_y, event.x, event.y, outline='red', tag='line')

    def on_release(event):
        nonlocal x, y, root
        x = event.x
        y = event.y
        pyautogui.screenshot('screenshot.png', region=(start_x, start_y, x - start_x, y - start_y))  # 截图
        root.destroy()

    root = tk.Tk()
    root.title('屏幕截图')
    root.overrideredirect(True)
    root.attributes("-alpha", 0.3)
    root.attributes("-topmost", True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.configure(background='black')

    canvas = tk.Canvas(root, bg='black', width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack()

    start_x = 0
    start_y = 0
    x = 0
    y = 0

    canvas.bind('<Button-1>', on_click)
    canvas.bind('<B1-Motion>', on_drag)
    canvas.bind('<ButtonRelease-1>', on_release)

    root.mainloop()

    screenshot = Image.open('screenshot.png')
    return screenshot

if __name__ == '__main__':
    # 使用示例：
    screenshot = capture_screenshot()
    screenshot.show()