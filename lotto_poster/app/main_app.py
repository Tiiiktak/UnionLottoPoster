import uvicorn
from fastapi import FastAPI
from routing import crawler_router, poster_router
from static import StaticImageService
from lotto_poster.utils import AppConfig


app = FastAPI()

app.include_router(crawler_router)
app.include_router(poster_router)

if __name__ == '__main__':
    StaticImageService.start_scheduler()
    uvicorn.run(app, host=AppConfig.host, port=AppConfig.port)
