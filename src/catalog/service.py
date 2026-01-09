import json

from odmantic import ObjectId

from src.aws.s3 import get_object
from src.config import settings


async def get_catalog_by_id(id: ObjectId) -> dict:
    return json.loads(get_object(settings.S3_BUCKET_NAME, id))
