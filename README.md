# Line_Bot_Flask_Example

**網路上目前多半為舊版程式，
所以本人撰寫了 Line Bot API v3.0 與 Line Notify API 的簡易範例程式**


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
- LINE_NOTIFY_TOKEN 位置：
![LINE_NOTIFY_TOKEN](https://media.discordapp.net/attachments/628539882503143428/1188112957255733400/python-line-notify-send-alert-message-tutorial-examples-20220528-03.png?ex=6599576b&is=6586e26b&hm=2eba0227e8e5eec18dbfee78afe8a0992d4f16c0b6e3c89ec771b38adf8828c9&=&width=1510&height=1092)

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
3-3. 當執行上述指令後會看到類似下列命令列：
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

### 6. 下載 Ngrok，並放置於「專案根目錄」

下載網址：[下載 Ngrok](https://ngrok.com/download)
![](https://media.discordapp.net/attachments/628539882503143428/1188119022915551353/2023-12-23_10.00.23.png?ex=65995d11&is=6586e811&hm=3560adfc4c7c62747fe9fec030a28df8fcc6fd5ce0284558f5419942cd4a6a99&=&width=1524&height=1016)

----

