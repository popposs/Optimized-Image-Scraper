from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

username = os.environ['POSTGRES_USERNAME']
host = os.environ['HOST_NAME']
port = os.environ['DB_PORT']
db = os.environ['DB_NAME']

if port:
    port = ":" + port

db_url = 'postgresql+psycopg2://{username}@{host}{port}/{db}'.format(username=username, \
                                                                host=host, \
                                                                port=port, \
                                                                db=db)

engine = create_engine(db_url)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
db = Session()

Base = declarative_base()
