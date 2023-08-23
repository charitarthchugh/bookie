from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from .database import Base, engine

"""Database Models"""


class Bookmark(Base):
    __tablename__ = "bookmarks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    url: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Optional[str]]
    added: Mapped[int]
    icon: Mapped[Optional[str]]
    folder: Mapped["Folder"] = relationship(back_populates="bookmarks")
    folder_id: Mapped[int] = mapped_column(ForeignKey('folders.id'))

    def __repr__(self):
        return f"<Bookmark(name={self.name}, url={self.url}, folder={self.folder})>"


class Folder(Base):
    __tablename__ = "folders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    name: Mapped[str]
    parent_id: Mapped[int]
    bookmarks: Mapped[list["Bookmark"]] = relationship(back_populates="folder")

    def __repr__(self):
        return f"<Folder(name={self.name}, parent_id={self.parent_id})>"


Base.metadata.create_all(engine)
