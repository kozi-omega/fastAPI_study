from typing import Optional
from pydantic import BaseModel, Field

# BaseModelを継承して、Pydanticモデルを作成
class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=20, example=["PC"]) # 最小文字数:2, 最大文字数:20
    price: int = Field(gt=0, lt=9999999, example=[100000]) # 0より大きく、9999999より小さい
    description: Optional[str] = Field(None, example=["備品です"]) # 任意項目

