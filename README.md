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
![LINE_NOTIFY_TOKEN](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/LINE_NOTIFY_TOKEN.png)

- LINE_BOT_API 位置：**Line Developers  ->  Message API**
![LINE_BOT_API](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/LINE_BOT_API.png)

- CHANNEL_SECRET 位置：**Line Developers  ->  Basic Settings**
![CHANNEL_SECRET](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/CHANNEL_SECRET.png)

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
![Ngrok Download](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/Ngrok%20Download.png)

![footer](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/footer.png)

----

### 7. 回到 Ngrok 官網，登入後到左側導覽列選「 Your Authtoken 」

![Ngrok Your Authtoken](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/Ngrok%20Your%20Authtoken.png)

----

### 8. 複製 Command Line 內容，在專案「根目錄」開啟 CMD，貼上指令並執行

![Command Line](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/Command%20Line.png)

![Command Line CMD](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/Command%20Line%20CMD.png)

----

### 9. 再回到 Ngrok 官網，到左側導覽列選「 Domains 」

![Domains](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/Domains.png)

----

### 10. 按下「 + New Domain 」

![New Domain](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/New%20Domain.png)

----

### 11. 網址出現後，按下「 Start a Tunnel 」

![Start a Tunnel](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/Start%20a%20Tunnel.png)

----

### 12. 按下複製按鈕，在專案「根目錄」開啟 CMD，貼上指令並更改 Port 號為 5000 後執行指令

![Copy Command](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/Copy%20Command.png)

![Command CMD](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/Command%20CMD.png)

----

### 13. 看到 Online 表示成功執行

![Ngrok Run](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/Ngrok%20Run.png)

----

### 14. 回到 Line Developers，到 Message API 頁面，在 Webhook URL 貼上剛剛 Ngrok 的網址，並在網址後方加上「 /callback 」，開啟「 Use webhook 」

![Webhook URL](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/Webhook%20URL1.png)

----

### 15. 等待 1～2 分鐘後，按下「 Verify 」測試，出現「 Success 」表示 Bot 已上線

![Verify](https://github.com/Kevin0901/Line_Bot_Flask_Example/blob/main/img/Webhook%20URL2.png)
