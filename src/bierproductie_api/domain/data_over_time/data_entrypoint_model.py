"""Object-relational mapping between the data_over_time database table and it's
python counter part
"""

from bierproductie_api.core.db import DB


class Model(DB.Model):
    """Model.

    TODO(Add DOC)
    """

    __tablename__ = 'data_over_time'

    batch_id = DB.Column(DB.Integer(), nullable=False)
    measurement_ts = DB.Column(DB.DateTime(), primary_key=True)
    inserted_ts = DB.Column(DB.DateTime(),
                            default=DB.text('CURRENT_TIMESTAMP'))
    temperature = DB.Column(DB.Float())
    humidity = DB.Column(DB.Float())
    vibration = DB.Column(DB.Float())
    produced = DB.Column(DB.Integer())
    state = DB.Column(DB.Integer())
    rejected = DB.Column(DB.Integer())
