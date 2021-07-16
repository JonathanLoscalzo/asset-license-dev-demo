from pymongo import MongoClient
from pymongo.database import Database
import json
import os
from asset_manager.models.models import Asset, License


def connect_db(connection_string: str, database_name: str) -> Database:
    client = MongoClient(connection_string)
    return client.get_database(database_name)


def initialize(db: Database) -> None:

    data = json.load(
        open(os.getcwd() + "/src/asset_manager/data/fixtures.json")
    )["catalog"]

    if "initialized" in db.list_collection_names():
        return

    db.get_collection("initialized").insert_one({"data": "initialized"})

    assets = [Asset(**asset) for asset in data["assets"]]
    licenses = [License(**asset) for asset in data["licences"]]

    db.get_collection("assets").insert_many(map(dict, assets))
    db.get_collection("licenses").insert_many(map(dict, licenses))
