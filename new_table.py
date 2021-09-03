from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

# Define additional imports here
from datetime import datetime

BaseClass = declarative_base()


class NewTable(BaseClass):  # class can have any name
    """
    Represents table in database

    Column creation:
        Create column as an attribute of this class.
            e.g. column_name = Column(column_type, **kwargs)
        where kwargs:
            -   primary_key: bool,
            -   autoincrement: bool,
            -   nullable: bool,
            -   default: object.
    ...............
    For more info about:
    -   creating column:
        SEE https://docs.sqlalchemy.org/en/13/orm/tutorial.html#declare-a-mapping
    -    data types
        SEE https://docs.sqlalchemy.org/en/14/core/type_basics.html
    -   Column object parameters
        SEE https://docs.sqlalchemy.org/en/13/core/metadata.html#sqlalchemy.schema.Column
    """

    # name of your table is necessary
    __tablename__ = 'your_table_name'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)
