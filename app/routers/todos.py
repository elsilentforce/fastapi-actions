from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/items")

@router.get("/")
async def index():
    return { "message": "Index items" }

@router.post("/{item_id}")
async def create_item(item_id: int):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
