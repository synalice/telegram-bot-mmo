import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.config import DB_NAME, DB_LOGIN, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE


engine = sa.create_engine(f'{DB_NAME}://{DB_LOGIN}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
