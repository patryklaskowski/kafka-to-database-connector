import os
import sqlalchemy
import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from more_itertools import one


from importlib import import_module


class Database:
    def __init__(self):
        """Create instance of class to be used when defining tables"""
        # tell SQLAlchemy how you'll define tables and models
        self.Base = declarative_base()

    def connect(self, db_conn_url):
        # connect database
        self.engine = sqlalchemy.create_engine(db_conn_url)

    def _build_session(self):
        # create session factory
        self.sessionmaker = sqlalchemy.orm.sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )
        # set up scoped_session registry
        # #add ability to access scoped session registry (implicitly)
        self.session = self._init_scoped_session()

    def _init_scoped_session(self):
        """Create empty scoped session registry upon app startup"""
        return sqlalchemy.orm.scoped_session(
            self.sessionmaker
        )

    def load_table(self, table_dir):
        """Load table"""
        try:
            print("curdir: ", os.path.abspath(os.curdir))
            # scan database package for modules ends with '_table.py'
            table_modules = [filenames for filenames in os.listdir(table_dir) if filenames.endswith('_table.py')]
            print("table_modules: ", table_modules)
            # get name of table modules
            table_module = one(table_modules)
            print("table_module: ", table_module)
            # import
            x = f"{table_dir}.{table_module.split('.')[0]}"
            print(x)
            module = import_module(x, package=table_dir)

            # scan for Table class
            table = [obj for name, obj in inspect.getmembers(module, inspect.isclass) if issubclass(obj, self.Base)]

            # set table object as instance variable
            self.Table = one(table)

        except ValueError:

            raise ValueError(f"There has to be only 1 module with '_table.py extension with 1 class inside {table_dir}")

    def create_table(self):
        """Create mapped tables in the database"""

        # create table in the database
        self.Base.metadata.create_all(bind=self.engine)

        self._build_session()

    def insert(self, **kwargs):
        """Adds table object to the database"""
        try:
            new_row = self.Table(**kwargs)
            self.session.add(new_row)
            self.session.commit()
            self.session.remove()

        except IntegrityError as err:
            self.session.rollback()
            print(err)

