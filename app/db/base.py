from sqlalchemy.ext.declarative import declarative_base

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# Database connection URL
DB_URL = os.environ.get('DATABASE_URL')
if DB_URL is None:
    raise ValueError('DATABASE_URL environment variable not set')

# Create the database engine
engine = create_engine(DB_URL)

# Create a session factory
Session = sessionmaker(bind=engine)
