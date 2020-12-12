""" Object-relational mapping between the maintenance database table and it's
python counter part
"""
from bierproductie_api.core.db import DB


class Model(DB.Model):
    """Model.

    TODO(Add DOC)
    """

    __tablename__ = 'maintenance'

    value = DB.Column(DB.Float(), default=DB.text('0'))
    updated_ts = DB.Column(DB.DateTime(), default=DB.text('CURRENT_TIMESTAMP'))
