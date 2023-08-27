import requests
import json
import pyperclip
import keyboard
import time

def past():
    keyboard.press_and_release("ctrl + v")
    time.sleep(0.1)
    keyboard.press_and_release('enter')

def nextline():
    keyboard.press_and_release("ctrl + enter")

def paste(message):
    pyperclip.copy(message)
    keyboard.press_and_release("ctrl + v")

# 将文本复制到剪贴板
def send_group_message(message):
    pyperclip.copy(message)
    # 模拟粘贴操作（Ctrl + V）
    keyboard.press_and_release('ctrl + v')
    time.sleep(0.1)
    keyboard.press_and_release('enter')

def send_group_message1(message):
    CQHTTPAPIURL = "http://127.0.0.1:5700/send_group_msg"

    GroupID = 832948295  # 替换为目标群的ID
# 构建请求体
    payload = {
        "group_id": GroupID,
        "message": message
    }

    # 发送 POST 请求
    try:
        response = requests.post(CQHTTPAPIURL, json=payload)
        response.raise_for_status()  # 检查是否有错误
        print("Message sent successfully!")
    except requests.exceptions.RequestException as e:
        print("Error:", e)


def main(message):
    send_group_message(message)


if __name__ == "__main__":
    main("Hello, this is a message from Python via Go-CQHTTP!")
