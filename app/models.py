from tortoise import Model
from tortoise import fields


class Offer(Model):
    id = fields.IntField(primary_key=True)
    desc = fields.TextField()

    class Meta:
        table = "offers"
