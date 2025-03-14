import redis

# 連接 Redis (Docker Redis 172.17.0.2)
client = redis.StrictRedis(host='host.docker.internal', port=6379, db=0, decode_responses=True)
# client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# 創建一個 "users" Table，使用 Redis 的 Hash 結構來存放用戶資料
def create_user(user_id, name, age):
    user_key = f"user:{user_id}"  # Redis 的 key，例如 user:1, user:2
    client.hset(user_key, mapping={"name": name, "age": age})
    print(f"User {name} created!")

# 讀取用戶資料
def get_user(user_id):
    user_key = f"user:{user_id}"
    user_data = client.hgetall(user_key)
    if user_data:
        print(f"User {user_id}: {user_data}")
    else:
        print(f"User {user_id} not found.")

# 刪除用戶
def delete_user(user_id):
    user_key = f"user:{user_id}"
    client.delete(user_key)
    print(f"User {user_id} deleted.")

# 測試插入資料
create_user(1, "Alice", 25)
create_user(2, "Bob", 30)

# 測試讀取資料
get_user(1)
get_user(2)

# 測試刪除資料
delete_user(1)
get_user(1)
