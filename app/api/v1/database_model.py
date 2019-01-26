#!/usr/bin/env python3
""" Database Manager  """
import sys
import psycopg2
from flask import current_app


class DatabaseManager:
    """ Routines for user to interact with the API database """
    def __init__(self):
        self.conn = None
        self.users_table_query = "CREATE TABLE IF NOT EXISTS users (\
            userid SERIAL PRIMARY KEY, \
            username VARCHAR(25) UNIQUE NOT NULL,\
            firstname VARCHAR(50) NOT NULL, \
            lastname VARCHAR(50) NOT NULL, \
            email VARCHAR(50) UNIQUE NOT NULL, \
            login_status BOOLEAN NOT NULL, \
            registration_timestamp VARCHAR(50) NOT NULL, \
            last_login_timestamp VARCHAR(50) NOT NULL, \
            password VARCHAR NOT NULL \
            );"

    def connect_to_db(self):
        """ Create connection to database and return cursor """
        try:
            self.conn = psycopg2.connect(current_app.config['DATABASE_URI'])
            db_cur = self.conn.cursor()
        except psycopg2.DatabaseError as err:
            db_cur = None
            print(f"Error connecting to DB: {err}")
        return db_cur

    def close_db(self):
        """ Closes database connection """
        if self.conn:
            self.conn.close()

    def save_db(self):
        """ Saves database's current state """
        if self.conn:
            self.conn.commit()

    def create_tables(self):
        """ Create database table """
        curs = self.connect_to_db()
        try:
            curs.execute(self.users_table_query)
            self.conn.commit()
            self.save_db()
            self.close_db()
            print('Tables created successfully!')
        except psycopg2.DatabaseError as err:
            self.db_error_handler(err)

    def drop_tables(self):
        """ Deletes database tables """
        curs = self.connect_to_db()
        try:
            curs.execute("DROP TABLE IF EXISTS users CASCADE")
            self.save_db()
            self.close_db()
        except psycopg2.DatabaseError as err:
            self.db_error_handler(err)

    def db_error_handler(self, error):
        """ Roll back transaction and exit incase of error """
        if self.conn:
            self.conn.rollback()
            print('An Error Occured: {}'.format(error))
            sys.exit(1)
