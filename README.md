# TwitchChatTTS

[English](README.md) [繁體中文](README-zh-tw.md)

![TwitchChatTTSLogo](Photo/Twitch%20Chat%20TTS%20Logo.png)

Using pyTwitchAPI and gTTS to transcript Twitch Chat Messages.

## Installation

Download this repository.

Install [Python](https://www.python.org/) in your Computer.

Open the current folder in terminal and create a virtual enviroment.

`python -m venv .virtualenv`

And Source the virtualenviroment

Windows :  `.\.virtualenv\Scripts\Activate.ps1`

Linux : `source ./.virtualenv/bin/acitvate`

And install the requirement for the application to run

`pip install -r requirements.txt`

### Optional

If you want to change the talking speed.

Download [ffmpeg](https://www.ffmpeg.org/) and put into current directory.

## Setting Up!

Go to [Twitch Developer Panel](https://dev.twitch.tv/console)

Click on Register a new application

![Register A New Application Twitch](Photo/Twitch%20Register%20a%20New%20Application.png)

You can name the Application whatever you want.

But the redirect URLs Must set to

`http://localhost:17563`

To make the Twitch authenticator working.

After Register the Application Paste the Client ID and Client Secret into conifg.json

```
    "APP_ID": "Client ID here",
    "APP_SECRET": "Client Secret Here",
```

Now Execucte the command `python start.py` should be starting the bot.

You will seeing the Bot is asking permission to read the chat.

![Twitch Authcating the Application](Photo/Twitch%20Auth.png)

Click on Authrize! and the bot should be greeting you for using the Bot!

## General Settings

```
    "TARGET_CHANNEL": "blusewill",
    "Language": "zh-TW",
    "Speed": "1.2"
    "Ignored_user": ["Nightbot", "Moobot", "StreamElements", "Streamlabs", "Fossabot"]
```

`TARGET_CHANNEL`

The Channel you're going to join to read the Chat

`Language`

The language you're going to use for TTS

Check the [gTTS Documentation](https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang) for the language you can currently use

`Speed`

The TTS Talking Speed.

Note : Require [ffmpeg](https://ffmpeg.org) to work

`Ignored_user`

The user that is going to be ignored in TTS function.