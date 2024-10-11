from fastapi import FastAPI
from routers import item_router
from routers import clock_in_router

app = FastAPI()

app.include_router(item_router.router)
app.include_router(clock_in_router.router)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to fastapi crud app!"}
