# Line_Bot_Flask_Example

**網路上目前多半為舊版程式，
所以本人撰寫了 Line Bot API v3.0 與 Line Notify API 的簡易範例程式**

**並使用 Ngrok 來開啟本地 Line Bot 服務**

**有疑問歡迎 Discord 聯絡：zaphkiel_0901**

# 操作步驟
### 0. 安裝 Python，安裝時記得勾選「Add Python 3.X to PATH」

下載網址：[下載 Python](https://www.python.org/downloads/)

----

### 1. 申請 Line Bot API 與 Line Notify API
申請 Line Bot API 參考文章：[建立 LINE Channel](https://steam.oxxostudio.tw/category/python/example/line-developer.html)

申請 Line Notify API 參考文章：[取得 LINE Notify 權杖](https://officeguide.cc/python-line-notify-send-messages-images-tutorial-examples/)

----

### 2. 下載此 GitHub 專案後，在「根目錄」新增 .env 檔存放 API 金鑰
```env
LINE_NOTIFY_TOKEN = 
LINE_BOT_API = 
CHANNEL_SECRET = 
```
- LINE_NOTIFY_TOKEN 位置 ( 請自行記住，Token 只會出現一次 )：
![LINE_NOTIFY_TOKEN](https://media.discordapp.net/attachments/628539882503143428/1188298607288385716/python-line-notify-send-alert-message-tutorial-examples-20220528-03.png?ex=659a0451&is=65878f51&hm=548831c1b99b2bfa8065359957d4acdae62411896b8e1356a8e1c5f2ffb3dec4)

- LINE_BOT_API 位置：**Line Developers  ->  Message API**
![LINE_BOT_API](https://media.discordapp.net/attachments/628539882503143428/1188115163883253792/2023-12-23_9.43.16.png?ex=65995979&is=6586e479&hm=07d12b6d81084f89b4471e40ae17e6bcb0a55582c1db442c69919ede936979ce&=&width=1986&height=304)

- CHANNEL_SECRET 位置：**Line Developers  ->  Basic Settings**
![CHANNEL_SECRET](https://media.discordapp.net/attachments/628539882503143428/1188116156863750244/2023-12-23_9.48.41.png?ex=65995a65&is=6586e565&hm=c9d0bb51a421e683fc695e1f37dbf3936d44438b085a880065b555fb48312059&=&width=1986&height=516)

----

### 3. 在專案「根目錄」開啟 CMD，創建 virtualenv 虛擬環境
3-1. 安裝 virtualenv
```cmd
pip install virtualenv
```
3-2. 啟動 virtualenv 環境
```cmd
virtualenv venv
```
3-3. 當執行上述指令後會看到 類似 下列命令列：
```cmd
(venv) C:\>
```

----

### 4. 在「虛擬環境」安裝所需的 Python 套件
```cmd
(venv) pip install -r requirements.txt
```

----

### 5. 執行專案
```cmd
(venv) python app.py
```

----

### 6. 下載 Ngrok，解壓縮後 EXE 檔放置於「專案根目錄」

網址：[下載 Ngrok](https://ngrok.com/download)
![Ngrok Download](https://media.discordapp.net/attachments/628539882503143428/1188119022915551353/2023-12-23_10.00.23.png?ex=65995d11&is=6586e811&hm=3560adfc4c7c62747fe9fec030a28df8fcc6fd5ce0284558f5419942cd4a6a99&=&width=1524&height=1016)

![footer](https://media.discordapp.net/attachments/628539882503143428/1188137841344118784/image.png?ex=65996e97&is=6586f997&hm=31a295032151eef44c2251d6a5530f1da4ce7825fe024c76c0e1a1e90899b117&=&width=1256&height=394)

----

### 7. 回到 Ngrok 官網，登入後到左側導覽列選「 My Authtoken 」

![Ngrok My Authtoken](https://media.discordapp.net/attachments/628539882503143428/1188139863959158884/image.png?ex=6599707a&is=6586fb7a&hm=4faa20f56aeaaf7adb3f23a55ba335ef70d85dd9ef8aff6af95767d8b0985114&=&width=524&height=940)

----

### 8. 複製 Command Line 內容，在專案「根目錄」開啟 CMD，貼上指令並執行

![Command Line](https://media.discordapp.net/attachments/628539882503143428/1188140195099443260/CommandKine.png?ex=659970c9&is=6586fbc9&hm=bea66736255671c9950122f3126c079b64ac30d1a35694846e615cab9c434541&=&width=2206&height=340)

![Command Line CMD](https://media.discordapp.net/attachments/628539882503143428/1188140390201704478/image.png?ex=659970f7&is=6586fbf7&hm=768d04455e73aac2d55301ef7d195d0e767fb6198ad5339fa77255f6ceafd122&=&width=1708&height=88)

----

### 9. 再回到 Ngrok 官網，到左側導覽列選「 Domain 」

![Domain](https://media.discordapp.net/attachments/628539882503143428/1188140591545073734/image.png?ex=65997127&is=6586fc27&hm=71a961ee22972069b1b250c16c097ecd87c8a5dd7f353760e9517a453aade86f&=&width=472&height=1092)

----

### 10. 按下「 + New Domain 」

![New Domain](https://media.discordapp.net/attachments/628539882503143428/1188140669659787284/image.png?ex=6599713a&is=6586fc3a&hm=f63fd9f31bae1791d7d15f0b6fc5aa06a45dd3a97128aa8ba731af0327e0a311&=&width=2206&height=398)

----

### 11. 網址出現後，按下「 Start a Tunnel 」

![Start a Tunnel](https://media.discordapp.net/attachments/628539882503143428/1188140997172002866/image.png?ex=65997188&is=6586fc88&hm=19fb2a9c4af6a3e52a08e43dfa2ae14a6d5aaf8dadd79feb58b43a21682e07a7&=&width=2206&height=682)

----

### 12. 按下複製按鈕，在專案「根目錄」開啟 CMD，貼上指令並更改 Port 號為 5000 後執行指令

![Copy Command](https://media.discordapp.net/attachments/628539882503143428/1188141674707288155/image.png?ex=65997229&is=6586fd29&hm=92414f7d354d39cf0645c62950d0a741c38d46ea0f2ffa2cc9a3ec02a09eb958&=&width=974&height=410)

![Command CMD](https://media.discordapp.net/attachments/628539882503143428/1188142027343396924/image.png?ex=6599727d&is=6586fd7d&hm=47ca3382c5c6e5ab81147fe2b77475f96d1b0661b6927f6cb9572d808782214e&=&width=2206&height=218)

----

### 13. 看到 Online 表示成功執行

![Ngrok Run](https://media.discordapp.net/attachments/628539882503143428/1188318551132622868/image.png?ex=659a16e4&is=6587a1e4&hm=2b81c9f6b4b32497edc410e4ea1e9fd9ab1e30d3aa611e70bd07a01d4e4aba7d&=&width=1590&height=546)

----

### 14. 回到 Line Developers，到 Message API 頁面，在 Webhook URL 貼上剛剛 Ngrok 的網址，並在網址後方加上「 /callback 」，開啟「 Use webhook 」

![Webhook URL](https://media.discordapp.net/attachments/628539882503143428/1188296900517052476/2023-12-24_9.46.11.png?ex=659a02ba&is=65878dba&hm=785bf60158bb71e5a90f279e8042e8aabf6dd505e2f84ba2957e9be8792c4d11&=&width=1956&height=1092)

----

### 15. 按下「 Verify 」測試，出現「 Success 」表示 Bot 已上線

![Verify](https://media.discordapp.net/attachments/628539882503143428/1188297234584981604/2023-12-24_9.48.17.png?ex=659a030a&is=65878e0a&hm=ee43252a0f22533fc5aa6e2c13a76086e44118048970a893aac9fa3e5bfa9d64&=&width=1288&height=412)
