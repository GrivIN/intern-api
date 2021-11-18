import datetime as _dt
import sqlalchemy as _sql

import database as _database


class Joke(_database.Base):
    __tablename__ = "jokes"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    setup = _sql.Column(_sql.String, index=True)
    punchline = _sql.Column(_sql.String, index=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)