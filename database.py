from flask import g
import sqlite3

def connect_to_db():
    sql = sqlite3.connect('/Users/user/Desktop/final_project/final_project/crudapp.db')
    sql.row_factory = sqlite3.Row
    return sql


def get_database():
    if not hasattr(g, 'crudapp_db'):
        g.crudapp_db = connect_to_db()
    
    return g.crudapp_db