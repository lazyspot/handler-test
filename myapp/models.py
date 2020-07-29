import sqlalchemy
from sqlalchemy import Column
from sqlalchemy.types import DateTime, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/logs'
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
DBSession = sessionmaker(bind=engine)
DBSession = DBSession()

Base = declarative_base()


class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)  # auto incrementing
    logger = Column(String(16), index=True)  # the name of the logger. (e.g. myapp.views)
    level = Column(String(16), index=True)  # info, debug, or error?
    trace = Column(String(16), index=True)  # the full traceback printout
    msg = Column(String(16), index=True)  # any custom log you may have included
    created_at = Column(DateTime, default=func.now())  # the current timestamp

    def __init__(self, logger=None, level=None, trace=None, msg=None):
        self.logger = logger
        self.level = level
        self.trace = trace
        self.msg = msg

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        return "<Log: %s - %s>" % (self.created_at.strftime('%m/%d/%Y-%H:%M:%S'), self.msg[:50])


Base.metadata.create_all(bind=engine)