# Line_Bot_Flask_Example

**網路上目前多半為舊版程式，所以本人撰寫了 V3.0 的簡易範例程式**


# 前置作業
### 0. 安裝 Python，安裝時記得勾選「Add Python 3.X to PATH」

下載網址：[下載 Python](https://www.python.org/downloads/)

----

### 1. 申請 Line Bot API 與 Line Notify API
申請 Line Bot API 參考文章：[建立 LINE Channel](https://steam.oxxostudio.tw/category/python/example/line-developer.html)

申請 Line Notify API 參考文章：[取得 LINE Notify 權杖](https://officeguide.cc/python-line-notify-send-messages-images-tutorial-examples/)

----

### 2. 在「根目錄」新增 .env 檔存放 API 金鑰
```env
LINE_NOTIFY_TOKEN = 
LINE_BOT_API = 
CHANNEL_SECRET = 
```

----

### 3. 在「根目錄」開啟 CMD，創建 virtualenv 虛擬環境
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

