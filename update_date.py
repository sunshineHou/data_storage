# @ author sunshine
# -*- coding: UTF-8 -*-
from create_table import Note, create_cursor
import time

def update(data):
    session = create_cursor()
    date = time.strftime('%Y-%m-%d', time.localtime())
    data_obj = Note(date=date, content=data)
    try:
        session.add(data_obj)
        session.commit()
    except Exception as e:
        return e
    else:
        return "Data upload success"

if __name__ == "__main__":
    update(data="")