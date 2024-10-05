from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SofaScoreData(Base):
    __tablename__ = 'sofa_score_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    incident_type = Column(String, nullable=True)
    time = Column(Integer, nullable=True)
    player_name = Column(String, nullable=True)
    home_score = Column(String, nullable=True)
    away_score = Column(String, nullable=True)

def create_tables(engine):
    Base.metadata.create_all(engine)
