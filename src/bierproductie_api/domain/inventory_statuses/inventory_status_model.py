"""Object-relational mapping between the inventory_statuses database table and
it's python counter part
"""

from bierproductie_api.core.db import DB


class Model(DB.Model):
    """Model.

    TODO(Add DOC)
    """

    __tablename__ = 'inventory_statuses'

    name = DB.Column(DB.String(128), primary_key=True)
    max_value = DB.Column(DB.Float())
    current_value = DB.Column(DB.Float())
