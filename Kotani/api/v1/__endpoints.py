from ninja import Router
from typing import List

router = Router()

@router.post("/recipes/batch", response=List[dict])
def create_recipes_batch(request):
    return [{"message": "POST endpoint called"}]

@router.put("/recipes/batch", response=List[dict])
def update_recipes_batch(request):
    return [{"message": "PUT endpoint called"}]

@router.get("/test", response=List[dict])
def test_endpoint(request):
    return [{"message": "GET endpoint called"}]