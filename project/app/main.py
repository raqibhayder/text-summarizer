from fastapi import FastAPI, Depends

from project.app.config import Settings, get_settings

app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "message": "Hello World",
        "environment": settings.environment,
        "testing": settings.testing,
    }
