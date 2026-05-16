from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Get database URL from environment variable (Render provides this)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# For PostgreSQL, we don't need check_same_thread
# Render's PostgreSQL URL format: postgresql://username:password@host:port/database
engine = create_engine(
    DATABASE_URL,
    pool_size=5,  # Maximum number of connections to keep
    max_overflow=10,  # Extra connections beyond pool_size
    pool_pre_ping=True,  # Verify connections before using
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()