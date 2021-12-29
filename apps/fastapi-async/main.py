from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.results import InsertOneResult

from config import settings
from message import Message


app = FastAPI()

mongodb_config = settings.get_mongodb_config()
client = AsyncIOMotorClient(**mongodb_config)
db: Database = client[settings.MONGODB_DATABASE]
collection: Collection = db[settings.MONGODB_COLLECTION_MESSAGES_NAME]


@app.post('/messages/', status_code=201, response_model=Message)
async def create_message(message: Message):
    message = jsonable_encoder(message)
    result: InsertOneResult = await collection.insert_one(message)

    if not result.acknowledged:
        raise HTTPException(status_code=500, detail='internal error.')

    return message
