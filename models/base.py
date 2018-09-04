from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

username = os.environ['DB_USER']
# password = os.environ['DB_PASSWORD']
host = os.environ['DB_HOST']
port = os.environ['DB_PORT']
db = os.environ['DB_NAME']

# if password:
#     password = ":" + password

if port:
    port = ":" + port

db_url = 'postgresql+psycopg2://{username}@{host}{port}/{db}'.format(username=username, \
                                                                host=host, \
                                                                port=port, \
                                                                db=db)

engine = create_engine(db_url)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

Base = declarative_base()
