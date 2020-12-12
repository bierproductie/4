"""Object-relational mapping between the batches database table and it's
python counter part
"""
from bierproductie_api.core.db import DB


class Model(DB.Model):
    """Model.

    TODO(Add DOC)
    """

    __tablename__ = 'batches'

    identifier = DB.Column(DB.Integer(), primary_key=True)
    speed = DB.Column(DB.Integer())
    amount_to_produce = DB.Column(DB.Integer())
    started_dt = DB.Column(DB.DateTime())
    recipe_id = DB.Column(DB.String(128))
    finished_dt = DB.Column(DB.DateTime())
    oee = DB.Column(DB.Float())
