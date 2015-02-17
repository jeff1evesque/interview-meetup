#!/usr/bin/python

## @db_query.py
#  This file contains logic required to select Meetup faves from the
#      database.
from package.database.db_query import SQL

## Class: Get_Fave, explicitly inherit 'new-style' class
class Get_Fave(object):

  ## constructor
  def __init__(self):
    self.list_error = []
    self.connector  = SQL()
