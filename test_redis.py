import redis

# 連接到 Podman Redis 容器
redis_host = "localhost"  # 或者是 Podman Redis 的 IP
redis_port = 6379
redis_password = None  # 如果 Redis 有設密碼，請填入

# 建立 Redis 連線
try:
    r = redis.Redis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    r.ping()
    print("成功連接到 Redis！")
except redis.ConnectionError as e:
    print(f"Redis 連線失敗: {e}")
    exit(1)

# 新增 (Create) 資料
def add_person(name, age, birthplace):
    r.hset(f"person:{name}", mapping={"name": name, "age": age, "birthplace": birthplace})
    print(f"已新增 {name} 的資料")

# 查詢 (Read) 資料
def get_person(name):
    person = r.hgetall(f"person:{name}")
    if person:
        print(f"{name} 的資料: {person}")
    else:
        print(f"找不到 {name} 的資料")

# 更新 (Update) 資料
def update_person(name, age=None, birthplace=None):
    if r.exists(f"person:{name}"):
        if age:
            r.hset(f"person:{name}", "age", age)
        if birthplace:
            r.hset(f"person:{name}", "birthplace", birthplace)
        print(f"已更新 {name} 的資料")
    else:
        print(f"找不到 {name}，無法更新")

# 刪除 (Delete) 資料
def delete_person(name):
    if r.delete(f"person:{name}"):
        print(f"{name} 的資料已刪除")
    else:
        print(f"找不到 {name} 的資料")

# 測試功能
if __name__ == "__main__":
    add_person("王小明", 18, "台北")
    get_person("王小明")

    update_person("王小明", age=19)
    get_person("王小明")

    delete_person("王小明")
    get_person("王小明")
