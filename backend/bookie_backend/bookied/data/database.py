import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

home = os.environ["HOME"]
path = Path(f"{home}/.local/share/bookie/bookie.sqlite")
if not path.exists():
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()
SQLITE_DB_URL = f"sqlite:///{path}"

engine = create_engine(SQLITE_DB_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
