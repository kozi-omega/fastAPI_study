from fastapi import FastAPI
from routers import item
"""
CRUD
Create, Read, Update, Deleteの頭文字を取ったもので、
ソフトウェア開発におけるデータ操作に不可欠な４つの操作
"""

app = FastAPI()
app.include_router(item.router)