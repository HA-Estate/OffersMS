from fastapi import APIRouter, Query, HTTPException

from app.models import Offer
from app.schemas import OfferSchema
from typing import Annotated
from app.crud import OfferCRUD

router = APIRouter(prefix="/offers", tags=["offers"])


@router.get("/")
async def get_all(
        limit: Annotated[int, Query()],
        offset: Annotated[int, Query()],
        prefetch: Annotated[bool, Query()] = False,
) -> list[OfferSchema]:
    return await OfferCRUD.get_all(prefetch, limit, offset)


@router.get("/{id_}")
async def get_by_id(id_: int):
    return await Offer.get_or_none(id=id_)


@router.get("/search")
async def get_by_query(q: Annotated[str, Query()]) -> list[OfferSchema]:
    raise HTTPException(500, "Not implemented")

@router.post("/")
async def create(payload: OfferSchema):
    return await Offer.create(**payload.model_dump())
