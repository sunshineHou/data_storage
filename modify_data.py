# @ author sunshine
# -*- coding: UTF-8 -*-
from create_table import Note, create_cursor

def modifyData(date,data):
    session = create_cursor()
    try:
        my_data = session.query(Note).filter_by(date="%s" % date).first()
        my_data.content = "%s" % data
        my_data.password = "HouZhicheng#2!"
        session.commit()
    except Exception as e:
        return e
    else:
        return "Data modification success"


if __name__ == '__main__':
    modifyData(date='',data='')