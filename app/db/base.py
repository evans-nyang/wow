import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
# Database connection URL
DB_URL = os.environ.get('DATABASE_URL')
if DB_URL is None:
    raise ValueError('DATABASE_URL environment variable not set')

# Create the database engine
engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
