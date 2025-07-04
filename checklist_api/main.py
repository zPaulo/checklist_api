from fastapi import FastAPI

from checklist_api.routers import auth, users

app = FastAPI(title='Minha API BALA!')

app.include_router(auth.router)
app.include_router(users.router)


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}
