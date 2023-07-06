'''
    This file is used to establish connection to the database
'''
from fastapi import Depends
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated

# 1. Creating URL to the database
DATABASE_NAME = 'BookApp'
USER_NAME = "root"
PWD = "Faizan26$"
HOST = "localhost"
PORT = "3306"

URL_DATABASE = f'mysql+pymysql://{USER_NAME}:{PWD}@{HOST}:{PORT}/{DATABASE_NAME}'

# 2. Create an engine
engine = create_engine(url = URL_DATABASE, echo = True)

#3. Create a session
session = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
    )

#4. Create a base class to create models
BASE = declarative_base()

#5. get Database
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close

#6. Create a dependency to automatically open and close db.
db_dependency = Annotated[Session, Depends(get_db)]