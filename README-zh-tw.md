# TwitchChatTTS

![TwitchChatTTSLogo](Photo/Twitch%20Chat%20TTS%20Logo.png)

[English](README.md) [繁體中文](README-zh-tw.md)

使用 pyTwitchAPI 和 gTTS 將 Twitch 聊天訊息轉為語音。

## 安裝

下載這個程式庫。

在電腦中安裝 [Python](https://www.python.org/)。

在終端機中開啟此專案的資料夾，並建立一個虛擬環境。

```
python -m venv .virtualenv
```

啟動虛擬環境：

- Windows:  
  ```
  .\.virtualenv\Scripts\Activate.ps1
  ```
- Linux:  
  ```
  source ./.virtualenv/bin/activate
  ```

安裝應用程式所需的套件：

```
pip install -r requirements.txt
```

### 可選設定

如果需要更改語音播放速度，可以安裝 [ffmpeg](https://www.ffmpeg.org/) 並將其放置在當前目錄中。

## 設定

前往 [Twitch 開發者面板](https://dev.twitch.tv/console)。

點擊「註冊新應用程式」。

![Register A New Application Twitch](Photo/Twitch%20Register%20a%20New%20Application.png)

應用程式名稱可隨意設定，但 **Redirect URLs** 必須設為：

```
http://localhost:17563
```

以啟用 Twitch 認證功能。

註冊完成後，將應用程式的 **Client ID** 與 **Client Secret** 貼到 `config.json` 中：

```
    "APP_ID": "Client ID here",
    "APP_SECRET": "Client Secret Here",
```

接著執行指令 `python start.py` 來啟動機器人。

此時應該會看到機器人請求讀取聊天室的權限。

![Twitch Authcating the Application](Photo/Twitch%20Auth.png)

點擊「Authorize!」授權後，機器人會向您打招呼並開始運作！

## 常規設定

```
    "TARGET_CHANNEL": "blusewill",
    "Language": "zh-TW",
    "Speed": "1.2",
    "Ignored_user": ["Nightbot", "Moobot", "StreamElements", "Streamlabs", "Fossabot"]
```

- **`TARGET_CHANNEL`**  
  指定要加入的頻道以讀取聊天訊息。

- **`Language`**  
  指定 TTS 使用的語言。  
  可參考 [gTTS 文件](https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang) 獲取目前支援的語言。

- **`Speed`**  
  TTS 的語音播放速度。  
  **注意**：需要安裝 [ffmpeg](https://ffmpeg.org) 才能使用此功能。

- **`Ignored_user`**  
  指定不會啟用 TTS 功能的使用者清單。