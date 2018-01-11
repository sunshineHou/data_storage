# @ author sunshine
# -*- coding: UTF-8 -*-
import sqlalchemy
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, sessionmaker

engine = create_engine("mysql+pymysql://sunshine:HouZhicheng#2!"
                       "@localhost:3306/mom_Informal_essay?charset=utf8",echo=True
                       )
metadata = MetaData()
note = Table('free_time_note', metadata,
             Column('id', Integer, primary_key=True, autoincrement=True),
             Column('date', String(20)),
             Column('content',String(1000))
             )

# note.create(bind=engine) # 建表

class Note():
    def __init__(self, date, content):
        self.id = 1
        self.date = date
        self.content = content

    def __repr__(self):
        return "<Note(id='%s', date='%s'" % (self.id, self.date)

mapper(Note, note)

def create_cursor():
    Session_class = sessionmaker(bind=engine)
    session = Session_class()
    return session

