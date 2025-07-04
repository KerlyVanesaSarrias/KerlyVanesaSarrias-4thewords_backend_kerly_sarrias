from fastapi import FastAPI
from app.core.database import init_db
from app.controllers.hello_controller import router as hello_router
from app.controllers.user_controller import router as auth_router

app = FastAPI()
init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)

app.include_router(hello_router)
app.include_router(auth_router)