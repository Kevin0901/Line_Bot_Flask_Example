# -*- coding:utf-8 -*-
import os, re, requests
from dotenv import load_dotenv

load_dotenv()

import flask
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent

app = flask.Flask(__name__)

# 放上自己的Channel Access Token，從 .env 讀取
api = os.getenv("LINE_BOT_API")
configuration = Configuration(access_token=api)

# 放上自己的Channel Secret，從 .env 讀取
channel = os.getenv("CHANNEL_SECRET")
handler = WebhookHandler(channel)


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = flask.request.headers["X-Line-Signature"]

    # get request body as text
    body = flask.request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info(
            "Invalid signature. Please check your channel access token/channel secret."
        )
        flask.abort(400)

    return "OK"


# 訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)

        # 使用者輸入的訊息
        message = event.message.text
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=message)],
            )
        )


# Line Notify 訊息發送
def Post_Msg(msg: str):
    headers = {
        "Authorization": "Bearer " + line_notify_token,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = {"message": msg}
    notify = requests.post(
        "https://notify-api.line.me/api/notify", headers=headers, params=payload
    )


if __name__ == "__main__":
    line_notify_token = os.getenv("LINE_NOTIFY_TOKEN")  # Line Notify 權杖
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
