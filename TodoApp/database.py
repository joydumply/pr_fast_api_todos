from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHAMY_DATABASE_URL='postgresql://mypostgresql_user:t"2dW0hxI,P^=+0tAZVM@localhost/todoapplicationdatabase'

engine = create_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()