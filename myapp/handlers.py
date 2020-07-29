import logging
import traceback
import sqlalchemy

from sqlalchemy import sql
from sqlalchemy import Column, MetaData
from sqlalchemy.types import DateTime, Integer, String
from sqlalchemy.sql import func, expression
from sqlalchemy.sql.expression import insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

import transaction

from models import Log, DBSession, Base, engine


class SQLAlchemyHandler(logging.Handler):
    # A very basic logger that commits a LogRecord to the SQL Db
    def emit(self, record):
        trace = None
        exc = record.__dict__['exc_info']
        if exc:
            trace = traceback.format_exc()
        log = Log(
            logger=record.__dict__['name'],
            level=record.__dict__['levelname'],
            trace=trace,
            msg=record.__dict__['msg'],)
        #print(log.__dict__)

        DBSession.add(log)
        transaction.commit()


