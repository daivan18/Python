import sys
import os

# ZeroMQ 通信模式
# PUB-SUB（發佈-訂閱）： 一個或多個發佈者向多個訂閱者發送消息。
# REQ-REP（請求-回應）： 客戶端發送請求，服務器回應。
# PUSH-PULL（推送-拉取）： 用於實現負載平衡，推送者將消息推送給多個拉取者處理。
# DEALER-ROUTER（經銷商-路由器）： 這是一種複雜的模式，通常用於需要更靈活消息路由的情境。

# 1.REQ-REP 模式：server/client\n 2.PUB-SUB 模式：pub/sub
# 由client發出請求，server接到請求後傳送回覆
# 終端機輸入指令說明：(開啟兩個終端機分別執行server和client)
# 1. REQ-REP 模式：
# python zeromq_main.py rep
# python zeromq_main.py req
# 2. PUB-SUB 模式：
# python zeromq_main.py pub
# python zeromq_main.py sub

# 加入 ZeroMQ 資料夾到模組搜尋路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
zeromq_path = os.path.join(current_dir, "ZeroMQ")
sys.path.append(zeromq_path)

# 匯入 Server 和 Client 模組
import rep
import req
import pub
import sub

def main():
    if len(sys.argv) < 2:
        print("請輸入 'server' 或 'client' 啟動對應的功能。")
        return

    mode = sys.argv[1].lower()
    # REQ-REP（請求-回應）
    if mode == "rep":
        rep.start_server()
    elif mode == "req":
        req.start_client()
    # PUB-SUB（發佈-訂閱）
    elif mode == "pub":
        pub.publisher()
    elif mode == "sub":
        sub.subscriber()
    else:
        print("無效參數！請使用 'server' 或 'client'。")

if __name__ == "__main__":
    main()
