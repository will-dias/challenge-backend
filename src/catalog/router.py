from fastapi import APIRouter, status
from odmantic import ObjectId

from src.catalog.schema import CatalogResponse
from src.catalog.service import get_catalog_by_id

router = APIRouter(prefix='/catalog', tags=['catalog'])


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=CatalogResponse)
async def get_catalog(id: ObjectId):
    return await get_catalog_by_id(id)
