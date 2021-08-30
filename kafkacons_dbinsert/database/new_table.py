# !!! These 2 imports are necessary
from sqlalchemy import *
from . import db

# Define additional imports here
from datetime import datetime


# !!! Class has to inherit from db.Base
class NewTable(db.Base):  # class can have any name

    """ A class represents table in database """

    # !!! name of your table is necessary
    __tablename__ = 'task001'

    """
    Column creation:
    
        Create column as an attribute of this class.
        column_name = Column(column_type, **kwargs)
    
        **kwargs:
    
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
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)
