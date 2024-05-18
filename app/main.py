import asyncio
from fastapi import FastAPI

from app import rabbitmq
from app.settings import settings
from app.endpoints.products_router import products_router


app = FastAPI(title='Products Service')


@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(rabbitmq.consume(loop))


app.include_router(products_router, prefix='/api')
