from config import settings
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


class MongoConnection:
    client: MongoClient = None
    database: Database = None

    def _get_collection(self, collection_name: str) -> Collection:
        return self.database[collection_name]

    @property
    def messasges(self) -> Collection:
        return self._get_collection('message')


mongo_connection = MongoConnection()


def connect_to_mongo():
    mongodb_config = settings.get_mongodb_config()

    mongo_connection.client = MongoClient(**mongodb_config)
    mongo_connection.database = mongo_connection.client[settings.MONGODB_DATABASE]


def close_mongo_connection():
    mongo_connection.client.close()
