import os
import time
import sqlalchemy
import inspect

from sqlalchemy.exc import IntegrityError, OperationalError
from more_itertools import one
from importlib import import_module


class Database:

    @classmethod
    def from_uri(cls, db_uri, base=None, timeout=30):
        print(f'\nTrying to create connection with {db_uri}\n')
        engine = sqlalchemy.create_engine(db_uri, echo=True, echo_pool=True, pool_pre_ping=True)
        cls.test_engine_connection(engine, timeout)
        print(f'\nConnection with {db_uri} successful!\n')
        return cls(engine, base)

    @staticmethod
    def test_engine_connection(engine, timeout=30):
        for t in range(1, timeout + 1):
            try:
                with engine.connect():
                    pass
            except OperationalError:
                print(f'Unsuccessful connection. {timeout-t} tries left.')
                time.sleep(1)
            else:
                return
        raise TimeoutError(f'Connection timeout {timeout}s. Connection with database unsuccessful.')

    def __init__(self, engine=None, base=None):
        """Create instance of class to be used when defining tables"""
        self.base_class = base
        self.engine = engine

        self.table_model = None
        self.Session = None

    def load_table_from(self, table_dir, endswith='_table.py'):
        """Load table"""

        curdir = os.path.abspath(os.curdir)
        scan_folder = os.path.join(curdir, table_dir)

        print(f'\n>>> Scanning "{scan_folder}" for Table schemas\n')
        table_modules = [filenames for filenames in os.listdir(scan_folder) if filenames.endswith(endswith)]
        print(f'>>> Found "{table_modules}" files with database schema in "{scan_folder}"')

        try:
            # Make sure only one exists
            table_module = one(table_modules)
        except ValueError:
            raise ValueError(f'Found multiple files ({table_modules}) endswith {endswith} in {scan_folder}. '
                             f'Should only one exist.') from None

        module_name = table_module.split('.')[0]  # new_table.py -> new_table
        address = f"{table_dir}.{module_name}"
        unique_attr = '__tablename__'

        print(f'>>> Scanning "{address}" for Table classes with unique attr "{unique_attr}"')
        module = import_module(address, package=table_dir)
        table_classes = [obj for name, obj in inspect.getmembers(module, inspect.isclass) if
                         hasattr(obj, unique_attr) and issubclass(obj, self.base_class)]
        print(f'>>> Found "{table_classes}" table classes in "{module}"')

        try:
            self.table_model = one(table_classes)
        except ValueError:
            raise ValueError(f'Found multiple classes ({table_classes}) with {unique_attr} in {module}. '
                             f'Should only one exist.') from None

        print(f'\n>>> Tablename {getattr(self.table_model, unique_attr)}\n')

    def create_loaded_table(self):
        """Create mapped tables in the database"""
        self.base_class.metadata.create_all(bind=self.engine)
        self._create_session()

    def _create_session(self):
        # Create session factory
        self.Session = sqlalchemy.orm.sessionmaker(bind=self.engine, autocommit=False, autoflush=False)

        # Contextual/Thread-local Sessions (user-defined Session scopes)
        # https://docs.sqlalchemy.org/en/13/orm/contextual.html
        # Further will create singleton instances of Session until Session.remove()
        # self.Session = sqlalchemy.orm.scoped_session(self.Session)

    def insert(self, **kwargs):
        """Adds table object to the database"""

        # TODO: Validate input prevent TypeError invalid keyword arg
        new_row = self.table_model(**kwargs)
        current_session = self.Session()
        current_session.add(new_row)
        try:

            current_session.commit()

        except IntegrityError as e:
            self.Session.rollback()
            raise IntegrityError from e
        except BaseException as e:
            raise BaseException('Unexpected exception occured.') from e
        else:
            return True
        finally:
            current_session.close()
