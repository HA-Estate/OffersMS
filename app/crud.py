from ms_core import BaseCRUD
from app.models import Offer
from app.schemas import OfferSchema


class OfferCRUD(BaseCRUD[Offer, OfferSchema]):
    model = Offer
    schema = OfferSchema
