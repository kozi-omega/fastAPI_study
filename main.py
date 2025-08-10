from fastapi import FastAPI, Body
from cruds import item as item_cruds
"""
CRUD
Create, Read, Update, Deleteの頭文字を取ったもので、
ソフトウェア開発におけるデータ操作に不可欠な４つの操作
"""


app = FastAPI()
# ----商品の読み込み(read:get)API----
@app.get("/items")
async def find_all():
    return item_cruds.find_all()

@app.get("/items/{id}")
async def find_by_id(id: int):
    return item_cruds.find_by_id(id)

@app.get("/items/")
async def find_by_name(name: str):
    return item_cruds.find_by_name(name)

# ----商品の登録(create:post)API----
@app.post("/items")
async def create(item_create=Body()):
    return item_cruds.create(item_create)

# ----商品の更新(update:put)API----
@app.put("/items/{id}")
async def update(id: int, item_update=Body()):
    return item_cruds.update(id, item_update)

# ----商品の削除(delete:del)API----
@app.delete("/items/{id}")
async def delete(id:int):
    return item_cruds.delete(id)