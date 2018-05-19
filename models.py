from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Words(Base):
    __tablename__ = 'words'

    word_id = Column(String(128), primary_key=True)
    word_text = Column(String(255), index=True, nullable=False, unique=True)
    word_count = Column(Integer())

class Links(Base):
    __tablename__ = 'links'

    url_id = Column(String(128), primary_key=True)
    url_text = Column(String(2048), primary_key=True)
    #cookie_recipe_url = Column(String(255))
    sentiment = Column(String(50))