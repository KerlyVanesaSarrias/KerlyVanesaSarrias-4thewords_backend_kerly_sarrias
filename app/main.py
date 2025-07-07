from fastapi import FastAPI
from app.core.database import init_db
from app.controllers.user_controller import router as auth_router
from app.controllers.legend_controller import router as legend_router
from app.controllers.category_controller import router as category_router
from app.controllers.location_controller import router as location_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)

app.include_router(auth_router)
app.include_router(legend_router)
app.include_router(category_router)
app.include_router(location_router)