from tortoise import Model
from tortoise import fields
from tortoise.contrib.postgres.indexes import GinIndex


class Offer(Model):
    id = fields.IntField(primary_key=True)
    desc = fields.TextField()

    class Meta:
        table = "offers"
        indexes = [GinIndex(fields={"desc"})]
