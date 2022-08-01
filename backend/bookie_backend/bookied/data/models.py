from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base, engine

"""Database Models"""


class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True, index=True)
    name = Column(String)
    description = Column(String)
    folder = relationship("Folder", back_populates="children")
    path = Column(String, ForeignKey("folders.path"))
    added = Column(Integer)


class Folder(Base):
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True, index=True)
    path = Column(String, index=True, unique=True)
    children = relationship("Bookmark", back_populates="folder")


Base.metadata.create_all(engine)
