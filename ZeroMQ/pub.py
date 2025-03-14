# publisher.py
import zmq
import time

def publisher():
    # 創建 ZeroMQ 上下文
    context = zmq.Context()
    
    # 創建 PUB 套接字，並綁定到指定的通訊端
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")  # 在 TCP 5555 端口上發佈消息

    print("Publisher is running...")

    count = 0
    while True:
        message = f"Message {count}"
        print(f"Sending: {message}")
        
        # 發送消息
        socket.send_string(message)
        
        count += 1
        time.sleep(1)  # 每秒發送一次

if __name__ == "__main__":
    publisher()
