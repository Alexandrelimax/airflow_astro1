import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL = os.getenv('DATABASE_URL')
URL = 'postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase'
class ConnectionPostgres:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ConnectionPostgres, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance


    def _initialize(self):
        self.engine = create_engine(URL)
        self.Session = sessionmaker(bind=self.engine)
        print("Conectado")


    def get_session(self):
        return self.Session()


    def close(self):
        self.engine.dispose()
