from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

Base = declarative_base()

# Category
class Order(Base):

    __tablename__ = "category"

    id = Column(Integer, primary_key=True, unique=True)
    
    region_ar = Column(String(32))
    region_en = Column(String(32))
    price = Column(Integer)
    
engine = create_engine('sqlite:///data_sqlite3.db')

engine = create_engine('sqlite:///data_db.sqlite3')

# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)



from sqlalchemy.orm import sessionmaker

session_factory = sessionmaker(bind=engine)

session = session_factory()