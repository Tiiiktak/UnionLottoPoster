import uvicorn
from fastapi import FastAPI
from routing import crawler_router
from lotto_poster.utils import AppConfig

app = FastAPI()

app.include_router(crawler_router)

if __name__ == '__main__':
    uvicorn.run(app, host=AppConfig.host, port=AppConfig.port)
