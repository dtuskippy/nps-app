# all of my obvious imports
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# have fire up this function in order to access the variable in .env
load_dotenv()

# accessing the environment variable in .env
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")

# establishing database connection, similar to mongoose.connect
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# manages individual database sessions per request (Mongoose does this automatically behind the scenes)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# he base class your models inherit from (in Mongoose, each model just uses mongoose.model directly)
Base = declarative_base()

# opens and closes a session for each request (Mongoose handles this invisibly)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()