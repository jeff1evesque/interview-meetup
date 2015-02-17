#!/usr/bin/python

## @db_query.py
#  This file contains logic required to add, or remove Meetup faves from the
#      database.
from datetime import datetime
from package.database.db_query import SQL

## Class: Adjust_Fave, explicitly inherit 'new-style' class
class Adjust_Fave(object):

  ## constructor
  def __init__(self):
    self.list_error = []
    self.connector  = SQL()

  ## db_initialize: creates the database, and tables
  def db_initialize(self):

    # create connection to sql
    self.connector.sql_connect()

    # create 'db_my_faves' database if doesn't exist
    sql_statement = 'CREATE DATABASE IF NOT EXISTS db_my_faves CHARACTER SET utf8 COLLATE utf8_general_ci'
    self.connector.sql_command( sql_statement, 'create' )

    # end connection to sql
    self.connector.sql_disconnect()
