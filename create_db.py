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

def create_movies_table():
    """Creates the movie table in the database"""
    con = sqlite3.connect('bond_movies.db')
    cur = con.cursor()
    movies_query = """CREATE TABLE IF NOT EXISTS movies
                        (Year INTEGER,
                        Movie TEXT NOT NULL,
                        Bond TEXT NOT NULL,
                        Avg_User_IMDB REAL);"""
    cur.execute(movies_query)
    con.commit()
    con.close()
    return

def populate_movies_table():
    """Populates the movies table with data from jamesbond.csv"""
    con = sqlite3.connect('bond_movies.db')
    cur = con.cursor()
    add_movie_query = """INSERT INTO movies (
                            Year,
                            Movie,
                            Bond,
                            Avg_User_IMDB
    )
    VALUES (?, ?, ?, ?)"""

    if not os.path.exists('jamesbond.csv'):
        print("Error: jamesbond.csv not found.")
        return
    
    bond_df = pd.read_csv('jamesbond.csv')

    for row in bond_df.itertuples(index=False):
        cur.execute(add_movie_query, (row.Year, row.Movie, row.Bond, row.Avg_User_IMDB))
    con.commit()
    con.close()
    return

if __name__ == '__main__':
    main()