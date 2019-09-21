import logging

from .entities import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Repository:

    def __init__(self, connection_string):
        self.logger = logging.getLogger("smartgrambot__repository")
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s"))

        engine = create_engine(connection_string, echo=False)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        self._session = session()
