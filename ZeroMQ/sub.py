# subscriber.py
import zmq

def subscriber():
    # 創建 ZeroMQ 上下文
    context = zmq.Context()
    
    # 創建 SUB 套接字，並連接到發佈者的通訊端
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")  # 連接到發佈者的端口

    # 訂閱所有消息（空字串代表訂閱所有主題）
    socket.setsockopt_string(zmq.SUBSCRIBE, "")

    print("Subscriber is running...")

    while True:
        # 接收消息
        message = socket.recv_string()
        print(f"Received: {message}")

if __name__ == "__main__":
    subscriber()
