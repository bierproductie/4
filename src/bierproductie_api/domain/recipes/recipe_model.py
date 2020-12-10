"""Object-relational mapping between the recipes database table and it's
python counter part
"""


from bierproductie_api.core.db import DB


class Model(DB.Model):
    """Model.

    TODO(Add DOC)
    """

    __tablename__ = 'recipes'

    machine_id = DB.Column(DB.Float(), nullable=False)
    max_speed = DB.Column(DB.Integer())
    recommended_speed = DB.Column(DB.Integer())
    name = DB.Column(DB.String(128), primary_key=True)
