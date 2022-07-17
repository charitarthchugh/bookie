from typing import Any, Union

from sqlalchemy.orm import Query, Session, session
from sqlalchemy.sql.functions import mode

from bookie_backend.data import models, schemas


def get_bookmark(db: Session, bookmark_id: int) -> Any:
    return db.query(models.Bookmark).filter(models.Bookmark.id == bookmark_id).first()


def get_bookmark_by_url(db: Session, bookmark_url: str):
    return db.query(models.Bookmark).filter(models.Bookmark.url == bookmark_url).first()


def create_bookmark(db: Session, bookmark: schemas.BookmarkCreate) -> models.Bookmark:
    # folder = get_folder_by_path(db, bookmark.path)
    db_bookmark = models.Bookmark(
        name=bookmark.name,
        description=bookmark.description,
        added=bookmark.added,
        url=bookmark.url,
        path=bookmark.path,
    )
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)
    return db_bookmark


def get_folder(db: Session, folder_id: int) -> Union[models.Folder, Any]:

    return db.query(models.Folder).filter(models.Folder.id == folder_id).first()


def get_folder_by_path(db: Session, folder_path: str) -> Union[models.Folder, Any]:

    return db.query(models.Folder).filter(models.Folder.path == folder_path).first()


def create_folder(db: Session, folder: schemas.FolderCreate) -> models.Folder:
    db_folder = models.Folder(path=folder.path)
    db.add(db_folder)
    db.commit()
    db.refresh(db_folder)
    return db_folder


def get_all_bookmarks(db: Session, skip: int = 0, limit: int = 100) -> list:
    return db.query(models.Bookmark).offset(skip).limit(limit).all()


def get_all_folders(db: Session) -> list:
    """
    Gets all the folders in the database
    """
    return db.query(models.Folder).all()
