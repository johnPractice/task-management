from bson import ObjectId


def checking_mongo_object_id(_id: str):
    return ObjectId.is_valid(_id)
