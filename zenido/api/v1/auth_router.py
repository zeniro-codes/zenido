from fastapi import APIRouter, status

auth_router = APIRouter()


@auth_router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user():
    pass
