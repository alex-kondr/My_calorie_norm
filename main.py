from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from src.routes import calorie


app = FastAPI()
app.include_router(calorie.router)

app.mount("/src/static", StaticFiles(directory="src/static"), name="static")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
