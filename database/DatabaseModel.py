from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, BOOLEAN, JSON, TIMESTAMP, FLOAT, ARRAY
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from sqlalchemy import Integer
from sqlalchemy import BOOLEAN
from sqlalchemy import String


Base = declarative_base()

class Proxy(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    data = Column(String(1000))
    # type = Column(String(20))
    # date_receiving = Column(DateTime)

def create_DB():
    engine = create_engine('sqlite://///Programming/Python/Carto.com/database/data.db')
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_DB()