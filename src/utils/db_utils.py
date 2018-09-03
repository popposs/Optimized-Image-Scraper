from sqlalchemy_utils.functions import create_database, drop_database
from sqlalchemy_utils.functions import database_exists
from models.base import Base, engine, db_url, db
import os

def create_tables():
    print("Creating new tables")
    Base.metadata.create_all(bind=engine)

def new_database():
    print("Creating new database")
    create_database(db_url)

def db_checks():
    if not database_exists(db_url):
       new_database()

    create_tables()

def erase_tables():
    meta = Base.metadata

    for table in reversed(meta.sorted_tables):
        if engine.dialect.has_table(engine, table.name):
            print('Clear table {}'.format(table.name))
            db.execute(table.delete())

    db.commit()
    db.close()

def reset_db():
    if not database_exists(db_url):
        new_database()

    erase_tables()
    create_tables()