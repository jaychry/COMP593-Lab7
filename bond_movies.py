"""
Description:
 Prints the Year, Movie and Bond actor of all movies in the Bond Movies database
 that were released before 1980 and saves the information to a CSV file.
 
 Usage:
  python early_bond_movies.py
"""
import os
import sqlite3
import pandas as pd

def main():
    early_movies_list = get_early_bond_movies()
    print_movies(early_movies_list)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    early_movies_csv = os.path.join(script_dir, 'early_bond_movies.csv')
    save_movies_to_csv(early_movies_list, early_movies_csv)

def get_early_bond_movies():
    """Queries the Bond Movies database for all movies released before 1980.
    Returns:
        list: (Year, Movie, Bond) of early Bond movies
    """
    con = sqlite3.connect("bond_movies.db")
    cur = con.cursor()
    cur.execute("SELECT Year, Movie, Bond FROM movies WHERE YEAR < 1980")
    early_movies = cur.fetchall()
    con.commit()
    con.close()
    return early_movies

