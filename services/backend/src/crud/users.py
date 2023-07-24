from fastapi import HTTPException
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.database.models import Users
from src.schemas.users import UserOutSchema
from src.schemas.token import Status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")


# these functions are going to be call in another module.
async def create_user(user)->UserOutSchema:
    user.password = pwd_context.encrypt(user.password)

    try:
        user_obj= await Users.create(**user.dict(exclude_unset=True))
    except IntegrityError:
        raise  HTTPException(status_code=401, detail=f"Sorry, that username already exist.") # is missing explain how detect that the username already exist
    
    return await UserOutSchema.from_tortoise_orm(user_obj)

async def delete_user(user_id, current_user)-> Status:
    try:
        db_user = await UserOutSchema.from_queryset_single(Users.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"user {user_id} not found")
    
    if db_user.id == current_user.id:
        delete_count= await Users.filter(id= user_id).delete()
        if not delete_count:
            raise HTTPException(status_code=404, datail=f"User {user_id} not found")
        return Status(message=f"Delete user {user_id}")
    
    raise HTTPException(status_code=403, detail=f"Not authorized to delete")