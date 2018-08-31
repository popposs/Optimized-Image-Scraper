from sqlalchemy import Column, String, Integer, MetaData, Table, Boolean
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.orm import relationship
import time

from models.base import Base

class URLS(Base):
    __tablename__ = "urls"
    url = Column('url', String(45), primary_key=True, autoincrement=False)
    host_path = Column('host_path', String(45))
