__all__ = ["db", "COLLECTIONS"]

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from .__base_config import MONGODB_URI, logger

DB_NAME = "eCommerce_petShop_app"
COLLECTIONS = ["products", "users"]
#DB_NAME = "bootcamp_eCommerce_app"
# COLLECTIONS = ["products", "users", "orders"]

# Create a new client and connect to the server
client = MongoClient(MONGODB_URI, server_api=ServerApi("1"))


# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    logger.info("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client[DB_NAME]

def create_collections() -> None:
    logger.warn("")                                 
    logger.info("Initializing collections...")
    for collection in COLLECTIONS:                  # por cada coleccion en nuestro array de collections
        if collection not in db.list_collection_names():            # si no existe la coleccion, la creo
            db.create_collection(collection)
            logger.info(f"\tCollection '{collection}' created.")
        else:
            logger.info(f"\tCollection '{collection}' already exists.")
    logger.warn("")

create_collections()        # cuando las colecciones ya existen hay que comentar esto