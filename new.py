import requests
import send
import time
import random
import pyperclip
import re

attempts = 0
time.sleep(0)
print("start")

def waitreply(st):
    ans=''
    s = requests.get('https://xiaobai.klizi.cn/API/other/gpt.php?msg=' + st, timeout=60).text
    s=remove_actual_backslashes(s)
    print(s)
    #if "你太美"in s:
    #    ans=s.split("你太美")
    #    s=''
    #    for i in ans:
    #        s=i+'鸡你太美'+s
    return str(s)

def remove_actual_backslashes(input_string):
    output_string = input_string.replace('\\n', '\n').replace('\\"', '"').replace("\\'", "'")
    return output_string

def get_response(message):
    response = ''
    response_raw = requests.get('https://xiaobai.klizi.cn/API/other/gpt.php?msg=' + message, timeout=60).text
    response = remove_actual_backslashes(response_raw)
    return str(response)

def send_message(text):
    send.send_group_message(text)

message_info = {"instruction_message": "message_seq", "group_id": "832948295", "message_id": ""}
group_id = message_info["group_id"]
url = "http://127.0.0.1:5700/get_group_msg_history?group_id=" + group_id
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36"
}

response_data = requests.get(url=url, headers=headers).json()
print(response_data)
last_message = response_data["data"]["messages"][len(response_data["data"]["messages"]) - 1]
print(last_message)
print("waiting...")
recommendation = last_message['message']
current_message = ''
wait_counter = 0
intervene = 0
exit_request_hash = 0
exit_verification = 0
group_change = 0
sum_answer = "0"
answer_count = 0
group_switch_id = 0
answer_mode = 0

while 1:
    try:
        response_data = requests.get(url=url, headers=headers).json()
        time.sleep(0.5)
        for message_info in response_data["data"]["messages"]:
            current_message = message_info["message"]
        if current_message == recommendation:
            continue
        elif response_data["data"]["messages"][len(response_data["data"]["messages"]) - 1]['post_type'] != 'message':
            continue
        elif exit_verification == 1:
            if current_message == exit_request_hash:
                send_message("hash验证成功")
                send_message("正在退出...")
                exit()
            else:
                send_message("hash验证失败")
                exit_verification = 0
            continue
        elif group_change == 1:
            if current_message == exit_request_hash:
                send_message("hash验证成功")
                send_message("正在更换群聊...")
                time.sleep(2)
                message_info = {"instruction_message": "message_seq", "group_id": group_switch_id, "message_id": ""}
                send_message("Change to" + group_switch_id + " done.")
            else:
                send_message("hash验证失败")
                group_change = 0
            continue
        elif current_message.split(" ")[0] == "/change":
            group_switch_id = current_message.split(" ")[1]
            exit_request_hash = str(time.time())
            print(exit_request_hash)
            send_message("确定你是主人：验证hash:ae867364-" + exit_request_hash)
            group_change = 1
        elif current_message.split(" ")[0] == "/menu":
            send_message("SkyBot菜单\n使用 /chat.c [询问的话] 呼唤chatGPT\n使用 /cat [询问的话] 呼唤cat\n使用 /stop 关闭插嘴功能\n使用 /rst 恢复插嘴功能")
            wait_counter = 0
        elif current_message.split(" ")[0] == "/help":
            send_message("♥输入/menu 查看菜单辣，什么？你想问我这名字谁起的？当然是我的主人***啦~")
            wait_counter = 0
        elif current_message.split(" ")[0] == "/chat.c":
            send_message("正在回答...")
            send_message(waitreply(current_message.split(' ')[1]))
            wait_counter = 0
        elif current_message.split(" ")[0] == "/cat":
            send_message("正在回答...")
            send_message(waitreply("假如你的名字叫cat，是个甜甜的bot，爱用颜文字特别是表情，这是群友刚刚的话，" + current_message.split(" ")[1] + "。说出你的回复"))
            wait_counter = 0
        elif current_message.split(" ")[0] == "/stop":
            send_message("好的，插嘴功能先关闭啦，想要叫我就用/rst指令哦~")
            intervene = 0
        elif current_message=="8":
            send_message("好孩子，真乖~")
        
        elif current_message.split(" ")[0] == "/rst":
            send_message("我回来啦~有事叫我哦~")
            intervene = 1
        elif wait_counter == 1 and answer_mode == 0:
            num1 = random.randint(0, 10)
            num2 = random.randint(0, 10)
            send_message("---Slow MATH---\n" + str(num1) + ' + ' + str(num2) + ' = ?')
            sum_answer = str(num1 + num2)
            answer_count = 0
            answer_mode = 1
        elif current_message.split(" ")[0] == "/exit":
            exit_request_hash = str(time.time())
            print(exit_request_hash)
            send_message("确定你是主人：验证hash:ae867364-" + exit_request_hash)
            exit_verification = 1
        elif current_message == '6':
            if 1:
                send_message('六真言?在我这里不管用!')
                wait_counter += 1
        elif "?" in current_message or "？" in current_message:
            send_message("?")
        elif current_message == "我是傻逼":
            send_message("管理！加精！")
        elif current_message=="wc":
            send_message("不要wc，操我")
        elif "笑死" in current_message:
            send_message("根本笑不死")
        elif "你妈" in current_message:
            send_message("我妈？")
        elif "[CQ:at,qq=3255996150]" in current_message:
            send_message("NTM不要@我可以吗")
        elif "傻逼" in current_message:
            send_message("hmm")
        elif "怎么你了" in current_message:
            send_message("怎么你了")
        elif "草泥马" in current_message:
            send_message("...")
        elif "你好" in current_message:
            send_message("好好，大家好")
        elif "好" in current_message:
            send_message("这就对了")
        elif current_message=="az":
            send_message("az")
        elif "牛逼" in current_message:
            send_message("草，6")
        elif current_message=="114514":
            send_message("野~兽~先~辈~")
        elif current_message=="鸡你太美":
            send_message("坤坤我爱你♥")
        elif current_message=="家人们谁懂啊":
            send_message("我不懂（狗头）")
        elif "射" in current_message:
            send_message("什么都射只会害了你")
        elif current_message == "草":
            send_message("草")
        elif "az" in current_message:
            send_message("az")
        elif "滚" in current_message:
            send_message("我滚了")
        elif "gun" in current_message:
            send_message("拜拜我滚了")
        elif waitreply("你是qq群的bot的控制单元，你被主人限制只能说出0或者1，1代表对当前言论反感，0代表不说话。这是刚刚的发言：" + current_message + '请输出')=='1':
            send_message("无语了家人们")
        elif waitreply("你是qq群的bot的控制单元，你被主人限制只能说出0或者1，1代表当前言论很无聊，枯燥，0代表不说话。这是刚刚的发言：" + current_message + '请输出')=='1':
            send_message("烦死我了")
        else:
            wait_counter += 1
            if intervene:
                choose = waitreply("你是一个qq群的bot的控制单元，你被主人限制只能说出0或者1或者2，1代表说话，0代表不说话，如果这是违法违规或者违背道德准则的事情回复2。这是刚刚的发言：" + current_message + '请输出')
                print(current_message, choose)
                if choose == '1':
                    send_message(waitreply("假如你的名字叫cat，是个甜甜的bot，爱用颜文字特别是表情，这是群友刚刚的话，" + current_message + "。说出你的回复"))
                if choose == '2':
                    send_message("你这是违法行为，走，跟我去自首~")
        if intervene:
            if wait_counter >= 10:
                send_message("@")
                time.sleep(1)
                send_message(response_data["data"]["messages"][len(response_data["data"]["messages"]) - 1]['sender']['nickname'])
                time.sleep(1)
                send_message(' 好久没跟我聊天了...陪我玩玩吧')
                wait_counter = 0
        else:
            if wait_counter >= 20:
                wait_counter = 0
        if current_message == sum_answer and answer_count <= 5 and answer_mode == 1:
                send_message("回答正确！不过主人懒得给我写奖励机制...")
                answer_count = 0
                sum_answer = "0"
                answer_mode = 0
        elif answer_count > 5:
            answer_count = 0
            sum_answer = "0"
            answer_mode = 0
        if answer_mode == 1:
            answer_count += 1
        recommendation = response_data["data"]["messages"][len(response_data["data"]["messages"]) - 1]['message']
        print(wait_counter)
    except Exception as e:
        try:
            send.send_group_message("出现错误，错误名："+str(e))
            ans+=1
            if ans>=5:
                exit()
        except:
            print(e)
        exitn=0
        change=0