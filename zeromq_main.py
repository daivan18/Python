import sys

# 終端機輸入指令說明：(開啟兩個終端機分別執行server和client)
# 1. python zeromq_main.py server
# 2. python zeromq_main.py client

# 加入 Time 資料夾到模組搜尋路徑
sys.path.append(r"C:\Users\p10368226\Documents\Python\side_project\ZeroMQ")

# 匯入 Server 和 Client 模組
import server
import client

def main():
    if len(sys.argv) < 2:
        print("請輸入 'server' 或 'client' 啟動對應的功能。")
        return

    mode = sys.argv[1].lower()
    if mode == "server":
        server.start_server()
    elif mode == "client":
        client.start_client()
    else:
        print("無效參數！請使用 'server' 或 'client'。")

if __name__ == "__main__":
    main()

