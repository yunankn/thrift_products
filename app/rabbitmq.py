import asyncio
import json
import traceback
from asyncio import AbstractEventLoop
from aio_pika.abc import AbstractRobustConnection
from aio_pika import connect_robust, IncomingMessage

from app.settings import settings
from app.services.products_service import ProductsService
from app.repositories.products_repo import ProductsRepo


async def process_comment_created(msg: IncomingMessage):
    try:
        data = json.loads(msg.body.decode())
        ProductsService(ProductsRepo()).create_comment(data['product_id'], data['text'])
        await msg.ack()
    except:
        traceback.print_exc()
        await msg.ack()


async def process_comment_rating_changed(msg: IncomingMessage):
    try:
        print(f"Got msg {msg}")
        data = json.loads(msg.body.decode())
        ProductsService(ProductsRepo()).update_comment_rating(data['comment_id'], data['delta'])
        await msg.ack()
    except:
        traceback.print_exc()
        await msg.ack()


async def consume(loop: AbstractEventLoop) -> AbstractRobustConnection:
    print("Starting RabbitMQ")
    await asyncio.sleep(5)
    connection = await connect_robust(settings.amqp_url, loop=loop)
    channel = await connection.channel()

    comment_created_queue = await channel.declare_queue('vodolazova_comment_created_queue', durable=True)
    comment_rating_changed_queue = await channel.declare_queue('vodolazova_comment_rating_changed_queue',
                                                               durable=True)

    print('Started RabbitMQ consuming...')
    await asyncio.gather(
        comment_created_queue.consume(process_comment_created),
        comment_rating_changed_queue.consume(process_comment_rating_changed)
    )
    return connection
