from fastapi import APIRouter

# create a new router instance
router = APIRouter()

# define a list of items
items = ["laptop", "phone", "tablet"]

# define a route to get the list of items - GET request
@router.get("/items/")
def read_items():
    # return the list of items
    return items

# define a route to create a new item - POST request
@router.post("/items/")
def create_item(item: str):
    # add the new item to the list
    items.append(item)
    # return the new item
    return {"item": item}
