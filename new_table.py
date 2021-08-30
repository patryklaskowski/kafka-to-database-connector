from sqlalchemy import *
from datetime import datetime
from database import db


class NewTable(db.Base):
    __tablename__ = 'xyz'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)
