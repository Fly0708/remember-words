import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.getenv('DATABASE_URL'), echo=True, echo_pool=True)

SessionLocal = sessionmaker(autoflush=False,expire_on_commit=False, bind=engine)
