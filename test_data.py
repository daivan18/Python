import redis

# 設定 Redis 連接參數
r = redis.Redis(host='host.docker.internal', port=6379, db=0, decode_responses=True)

# 儲存一些資料
r.set("name", "John Doe")
r.set("age", 30)
r.set("location", "New York")

# 讀取資料
name = r.get("name")
age = r.get("age")
location = r.get("location")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Location: {location}")
