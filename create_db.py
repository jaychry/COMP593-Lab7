"""
Description:
Creates the movies table in the Bond Movies database
and populates it with data from jamesbond.csv.

Usage:
 python create_db.py
"""
import os
import sqlite3
import pandas as pd

def main():
    con = sqlite3.connect('bond_movies.db')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, 'bond_movies.db')
    con.commit()
    cur = con.cursor()
    create_movies_table()
    populate_movies_table()
    con.close()

