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

  ## fave_intersection: given list of events (group ids), return the
  #                     intersection with stored favorite events with
  #                     respect to current user (uid).
  def fave_intersection( list_events, uid ):
