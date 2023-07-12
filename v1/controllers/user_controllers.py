from v1.models.user_models import User

async def get_users():
    return { "users": "test" }

async def get_user(userID: int):
    return { "user": userID }

async def create_user(user: User):
    return user