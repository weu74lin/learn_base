from fastapi import FastAPI
from pydantic import BaseModel
import json
app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

items = []

@app.get("/")
def hello():
    return 'hello'

@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    save()
    return item
'''post更新多条，然后get查询'''
#方法A:
#先post进行多次Execute添加多条，再get显示
#方法B：改成一次提交一个列表
# @app.post("/items/batch")
# def create_items(new_items: list[Item]):
#     items.extend(new_items)
#     return new_items

@app.get("/items/")
def list_items():
    return items

def save():
    # Json存储
    with open("Item_testdata.json", "w", encoding="utf-8") as f:
        from pprint import pprint
        pprint(items)
        
        json.dump(
            [item.model_dump() for item in items], 
            f,
            ensure_ascii=False, 
            indent=4
        )

