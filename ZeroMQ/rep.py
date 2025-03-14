import zmq

def start_server():
    # 建立 ZeroMQ 上下文
    context = zmq.Context()

    # 創建 REP (Reply) socket，並綁定到 tcp://*:5555
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("伺服器啟動，等待請求...")

    while True:
        # 接收請求
        message = socket.recv_string()
        print(f"收到請求: {message}")

        # 回傳回覆
        response = f"已收到：{message}"
        socket.send_string(response)
