import zmq
import time

def start_client():
    # 建立 ZeroMQ 上下文
    context = zmq.Context()

    # 創建 REQ (Request) socket，並連接到伺服器
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    for i in range(5):
        # 傳送請求
        message = f"Hello {i}"
        print(f"發送請求: {message}")
        socket.send_string(message)

        # 接收回覆
        response = socket.recv_string()
        print(f"收到回覆: {response}")

        time.sleep(1)  # 模擬處理間隔

