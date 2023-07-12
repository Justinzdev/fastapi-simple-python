from fastapi import APIRouter

# Controllers
from v1.controllers.user_controllers import get_users, get_user, create_user

# Models
from v1.models.user_models import User

router = APIRouter()

@router.get('/users')
async def read_users():
    return await get_users()

@router.get('/user/{userID}')
async def read_user(userID: int):
    return await get_user(userID)

@router.post('/user/create')
async def create_user_route(user: User):
    return await create_user(user)