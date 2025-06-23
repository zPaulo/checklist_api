from fastapi import FastAPI
from http import HTTPStatus
from checklist_api.schemas import UserSchema, UserPublic, UserDB

app = FastAPI()
database = []

@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    return user