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
