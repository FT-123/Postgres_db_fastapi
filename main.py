from fastapi import FastAPI
import auth.router
from database import Model, engine
from User import Usersrout

Model.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(Usersrout.router)
app.include_router(auth.router.router)




