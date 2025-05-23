from fastapi import APIRouter

router = APIRouter()

items = ["laptop", "phone", "tablet"]

@router.get("/items/")
def read_items():
    return items

@router.post("/items/")
def create_item(item: str):
    items.append(item)
    return {"item": item}
