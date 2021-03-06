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
  def fave_intersection(self, list_events, uid):

    # local variables
    list_intersection = []

    # create connection to sql
    self.connector.sql_connect('db_my_faves')

    for gid in list_events:
      # insert 'fave' into 'tbl_fave_gid'
      sql_statement = 'SELECT gid FROM tbl_fave_gid WHERE gid=%s AND uid_created=%s'
      args = (gid, uid)
      response = self.connector.sql_command( sql_statement, 'select', args )

      # append favorite event(s) from database query
      if response:
        if response['result']:
          list_intersection.append( response['result'][0][0] )

      # retrieve any error(s)
      if self.connector.return_error(): self.list_error.append( self.connector.return_error() )

    # end connection to sql
    self.connector.sql_disconnect()

    # return list of intersections
    return list_intersection

  ## get_db_error: return all error(s)
  def get_db_error(self):
    return self.list_error
