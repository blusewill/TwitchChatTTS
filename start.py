from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatEvent
import json
from playsound import playsound
from gtts import gTTS
import os
import time
import asyncio
import subprocess

PWD = os.getcwd()

with open(f'{PWD}\\config.json', 'r') as config_file:
    config = json.load(config_file)

APP_ID = config["APP_ID"]
APP_SECRET = config["APP_SECRET"]
TARGET_CHANNEL = config["TARGET_CHANNEL"]
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
Language = config["Language"]
Speed = config["Speed"]
Ignored_User = config["Ignored_User"]
ffmpeg_command = [f"{PWD}\\ffmpeg.exe", "-y", "-i", "temp.mp3", "-filter:a", f"atempo={Speed}", "TTS.mp3"]

async def play_tts(text: str):
    tts = gTTS(text, lang=Language)
    tts.save("temp.mp3")
    time.sleep(0.5)
    if Speed == '1':
        playsound("temp.mp3")
        time.sleep(0.5)
        os.remove("temp.mp3")
    else:
        subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        playsound('TTS.mp3')
        time.sleep(0.5)
        os.remove("temp.mp3")
        os.remove("TTS.mp3") 

async def on_ready(ready_event: EventData):
    if Language == "zh-TW":
        print(f'機器人已經在線上了！加入 {TARGET_CHANNEL} 的圖奇！')
    else:
        print(f"Bot is Currently Online! Joining {TARGET_CHANNEL}'s Twitch Channel.")
    
    await ready_event.chat.join_room(TARGET_CHANNEL)
    
    if Language == "zh-TW":
        await play_tts(f'{TARGET_CHANNEL} 安安，現在開始為你檢測聊天室訊息')
    else:
        await play_tts(f'Hello! {TARGET_CHANNEL}. Now Starting to Detecting the Twitch Chat Messages.')
    time.sleep(0.5)

async def on_message(msg: ChatMessage):
    if msg.user.name in Ignored_User:
        return
    elif msg.user.display_name in Ignored_User:
        return
    if Language == "zh-TW":
        print(f'{msg.user.display_name} 說了 {msg.text}')
    else:
        print(f'{msg.user.name} - {msg.text}')
    filtered_msg = msg.text
    check_emotes = msg.emotes
    if check_emotes:  # This checks if check_emotes is not None or empty
        ranges_to_remove = []
        for emote_key in msg.emotes:
            if isinstance(msg.emotes[emote_key], list):
                for emote in msg.emotes[emote_key]:
                    start = int(emote['start_position'])
                    end = int(emote['end_position']) + 1
                    ranges_to_remove.append((start, end))

        for start, end in sorted(ranges_to_remove, reverse=True):
            filtered_msg = filtered_msg[:start] + ' ' + filtered_msg[end:]
            filtered_msg = ' '.join(filtered_msg.split())
    
        if filtered_msg.lower() == '':
            return
        elif Language == "zh-TW":
            await play_tts(f'{msg.user.display_name} - {filtered_msg}')
            return
        else:
            await play_tts(f'{msg.user.name} - {filtered_msg}')
            return

    if 'http' in msg.text:
        if Language == "zh-TW":
            filtered_msg = ' '.join('連接看一下' if word.startswith('http') else word for word in msg.text.split())
        else:
            filtered_msg = ' '.join('Please Check the link.' if word.startswith('http') else word for word in msg.text.split())
        if Language == "zh-TW":
            await play_tts(f'{msg.user.display_name} - {filtered_msg}')
        else:
            await play_tts(f'{msg.user.name} - {filtered_msg}')
    
    elif "!" in msg.text:
        return
    else:
        if Language == "zh-TW":
            await play_tts(f'{msg.user.display_name} - {filtered_msg}')
        else:
            await play_tts(f'{msg.user.name} - {filtered_msg}')

    await asyncio.sleep(1)

async def run():
    twitch = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    chat = await Chat(twitch)

    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)

    chat.start()

    try:
        if Language == "zh-TW":
            input('按下 Enter 來關機\n')
        else:
            input('Press Enter to Shutdown\n')
    finally:
        chat.stop()
        await twitch.close()

if __name__ == "__main__":
    asyncio.run(run())
