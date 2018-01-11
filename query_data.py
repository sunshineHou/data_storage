# @ author sunshine
# -*- coding: UTF-8 -*-
from create_table import Note, create_cursor

def queryData(date=None):
    session = create_cursor()
    if id == None:
        my_data_list = session.query(Note).filter_by().all()
        return my_data_list
    else:
        my_data = session.query(Note).filter_by(date = "%s" % date).first()
        return my_data

if __name__ == "__main__":
    queryData()