import dataclasses
import random

from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()
NAMES = ["leo", "nikita", "alim", "mark", "sasha"]

@dataclasses.dataclass
class User:
    id: int
    name: str
    age: int


@dataclasses.dataclass
class Users:
    lists: list[User]


def create_obj() -> Users:
    users = Users([])
    for i in range(5):
        users.lists.append(User(i, NAMES[i], random.randint(10, 40)))
    return users


@router.get("/get_users")
async def get_users():
    return USERS


@router.get("/get_user_by_id/{id}")
async def get_user_by_id(id: int):
    for i in USERS.lists:
        if i.id == id:
            return i
    return -1


@router.post("/post_user")
async def post_user(user: User):
    USERS.lists.append(user)

@router.delete("/delete_user/{id}")
async def delete_user(id: int):
    USERS.lists.pop(id)


@router.put("/change_user_by_id")
async def change_user(user: User):
    global USERS
    for i in USERS.lists:
        if i.id == user.id:
            i.name = user.name
            i.age = user.age
            return
    return -1
app.include_router(router)

USERS = create_obj()
