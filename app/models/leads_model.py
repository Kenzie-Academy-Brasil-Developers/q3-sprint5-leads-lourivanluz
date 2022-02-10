from dataclasses import dataclass
from app.config.database_config import db
from sqlalchemy import Column,String,Integer,DateTime


@dataclass
class Leads(db.Model):

    __tablename__ = 'tb_leads'
     
    id:str = Column(Integer,primary_key=True)
    name:str = Column(String,nullable=False)
    email:str = Column(String,nullable=False,unique=True)
    phone:str = Column(String,nullable=False)
    creation_date:str = Column(DateTime)
    last_visit:str = Column(DateTime)
    visits:str = Column(Integer,default=1)


