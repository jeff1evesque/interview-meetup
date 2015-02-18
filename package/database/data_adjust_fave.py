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

    # retrieve any error(s), end connection to sql
    if self.connector.return_error(): self.list_error.append( self.connector.return_error() )
    self.connector.sql_disconnect()

    # create connection to sql
    self.connector.sql_connect('db_my_faves')

    # create 'tbl_fave_gid' if doesn't exist
    sql_statement = '''\
                    CREATE TABLE IF NOT EXISTS tbl_fave_gid (
                      id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                      gid INT NOT NULL,
                      uid_created INT NOT NULL,
                      datetime_modified DATETIME NOT NULL
                    );
                    '''
    self.connector.sql_command( sql_statement, 'create' )

    # retrieve any error(s), end connection to sql
    if self.connector.return_error(): self.list_error.append( self.connector.return_error() )
    self.connector.sql_disconnect()

  ## db_fave_add: add user selected Meetup fave to database
  #
  #  @gid, refers to the Meetup 'group_id'
  #  @uid, the 'user_id' associated with web-platform (i.e. CMS)
  def db_fave_add(self, gid, uid):

    # create connection to sql
    self.connector.sql_connect('db_my_faves')

    # insert 'fave' into 'tbl_fave_gid'
    sql_statement = 'INSERT INTO tbl_fave_gid (gid, uid_created, datetime_modified) VALUES( %s, %s, UTC_TIMESTAMP() )'
    args = (gid, uid)
    response = self.connector.sql_command( sql_statement, 'insert', args )

    # retrieve any error(s), end connection to sql
    if self.connector.return_error(): self.list_error.append( self.connector.return_error() )
    self.connector.sql_disconnect()

  ## db_fave_remove: remove user selected Meetup fave from database
  #
  #  @gid, refers to the Meetup 'group_id'
  #  @uid, the 'user_id' associated with web-platform (i.e. CMS)
  def db_fave_remove(self, gid, uid):

    # create connection to sql
    self.connector.sql_connect('db_my_faves')

    # delete 'fave' from 'tbl_fave_gid'
    sql_statement = 'DELETE FROM tbl_fave_gid WHERE gid=%s AND uid_created=%s'
    args = (gid, uid)
    response = self.connector.sql_command( sql_statement, 'delete', args )

    # retrieve any error(s), end connection to sql
    if self.connector.return_error(): self.list_error.append( self.connector.return_error() )
    self.connector.sql_disconnect()

  ## get_db_error: return all error(s)
  def get_db_error(self):
    return self.list_error
