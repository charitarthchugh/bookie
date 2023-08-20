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
    # path = Column(String, ForeignKey("folders.path"))
    parent_folder_id = Column(Integer, ForeignKey("folders.id"))
    added = Column(Integer)
    icon = Column(String)  # name of Icon, not the icon itself


class Folder(Base):
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    bookmarks = relationship("Bookmark", back_populates="folder")
    parent_folder_id = Column(Integer)


Base.metadata.create_all(engine)
