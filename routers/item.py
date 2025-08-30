from fastapi import APIRouter, Body
from cruds import item as item_cruds
from schemas import ItemCreate

# インスタンス化
router = APIRouter(prefix='/items', tags=['items'])

# ----商品の読み込み(read:get)API----
@router.get("")
async def find_all():
    return item_cruds.find_all()

@router.get("/{id}")
async def find_by_id(id: int):
    return item_cruds.find_by_id(id)

@router.get("/")
async def find_by_name(name: str):
    return item_cruds.find_by_name(name)

# ----商品の登録(create:post)API----
@router.post("")
async def create(item_create: ItemCreate):
    return item_cruds.create(item_create)

# ----商品の更新(update:put)API----
@router.put("/{id}")
async def update(id: int, item_update=Body()):
    return item_cruds.update(id, item_update)

# ----商品の削除(delete:del)API----
@router.delete("/{id}")
async def delete(id:int):
    return item_cruds.delete(id)