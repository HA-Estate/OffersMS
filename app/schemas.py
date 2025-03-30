from tortoise.contrib.pydantic import pydantic_model_creator
from app.models import Offer


OfferSchema = pydantic_model_creator(Offer, name="OfferSchema", exclude_readonly=True)

