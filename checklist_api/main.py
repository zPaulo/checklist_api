from http import HTTPStatus

from fastapi import FastAPI

from checklist_api.routers import auth, todos, users
from checklist_api.schemas import Message

app = FastAPI(title='Minha API BALA!')

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
