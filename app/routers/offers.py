from fastapi import APIRouter, Query

from app.models import Offer
from app.schemas import OfferSchema
from typing import Annotated

router = APIRouter(prefix="/offers", tags=["offers"])


@router.get("/{id_}")
async def get_by_id(id_: int):
    return await Offer.get_or_none(id=id_)


@router.get("/")
async def get_by_query(q: Annotated[str, Query()]) -> list[OfferSchema]:
    return await Offer.filter(desc__search=q)


@router.post("/")
async def create(payload: OfferSchema):
    return await Offer.create(**payload.model_dump())
