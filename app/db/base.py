import os

import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Database connection URL
DB_URL = os.environ.get('DATABASE_URL')
if DB_URL is None:
    raise ValueError('DATABASE_URL environment variable not set')

# Test database connection URL
# TEST_DB_URL = os.environ.get('TEST_DATABASE_URL')
# if TEST_DB_URL is None:
#     raise ValueError('TEST_DATABASE_URL environment variable not set')

# Create the database engine
engine = create_engine(DB_URL)

# Create the test database engine
# test_engine = create_engine(TEST_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

Base = declarative_base()

# Dependency injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency injection for test database
# @pytest.fixture(scope="module")
# def get_test_db():
#     db = TestSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
