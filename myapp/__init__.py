import logging

import models
import handlers
import views
from pyramid.config import Configurator
from models import DBSession, Base, engine

def main():
    logging.basicConfig(filename='log_tessadt.log')
    logging.getLogger('').addHandler(handlers.SQLAlchemyHandler())

    # Register MY_LOGGER
    log = logging.getLogger('MY_LOGGER')
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    log.addHandler(ch)

    log.setLevel("DEBUG")
    log.debug('debug message')
    log.info('info message')
    log.warning('warn message')
    log.error('error message')
    log.critical('critical message')
    Base.metadata.create_all(bind=engine)
if __name__ == "__main__":
    main()
