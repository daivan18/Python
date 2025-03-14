from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# 建立 FastAPI 應用
app = FastAPI()

# 定義資料模型
class Person(BaseModel):
    name: str
    age: int
    birthplace: str

# 模擬一個資料庫來儲存資料
people_db = []

# POST：新增多筆資料
@app.post("/new_people/")
def create_people(people: List[Person]):
    people_db.extend(people)
    return {"message": f"已新增 {len(people)} 筆資料"}

# GET：查詢所有資料
@app.get("/query_people/")
def get_people():
    return people_db
