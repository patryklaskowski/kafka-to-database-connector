from sqlalchemy import *
from datetime import datetime
from . import db


class NewTable(db.Base):
    __tablename__ = 'name_of_your_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)
