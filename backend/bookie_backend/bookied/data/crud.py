from typing import Optional, Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models, schemas
from .models import Folder


def get_bookmark(db: Session, bookmark_id: int) -> Optional[models.Bookmark]:
    # return db.query(models.Bookmark).filter(models.Bookmark.id == bookmark_id).first()
    return db.get(models.Bookmark, bookmark_id)


def get_bookmark_by_url(db: Session, bookmark_url: str) -> Optional[models.Bookmark]:
    return db.execute(select(models.Bookmark).where(models.Bookmark.url == bookmark_url)).scalar_one_or_none()


def create_bookmark(db: Session, bookmark: schemas.BookmarkCreate) -> models.Bookmark:
    db_bookmark = models.Bookmark(
        name=bookmark.name,
        description=bookmark.description,
        added=bookmark.added,
        url=bookmark.url,
        folder_id=bookmark.folder_id,
        icon=bookmark.icon)
    db.add(db_bookmark)
    db.commit()
    return db_bookmark


def get_folder(db: Session, folder_id: int) -> Optional[models.Folder]:
    return db.get(models.Folder, folder_id)


# def get_folder_by_path(db: Session, folder_path: str) -> Union[models.Folder, Any]:
#     return db.query(models.Folder).filter(models.Folder.path == folder_path).first()
# def get_folder_by_name(db: Session, name: str) -> Union[models.Folder, Any]:
#     return db.query(models.Folder).filter(models.Folder.name == name)


def get_folders_by_parent_id(db: Session, parent_id: int) -> Sequence[Folder]:
    # return db.query(models.Folder).filter(models.Folder.parent_folder_id == parent_id)
    return db.execute(select(models.Folder).where(models.Folder.parent_id == parent_id)).scalars().all()


def create_folder(db: Session, folder: schemas.FolderCreate) -> models.Folder:
    db_folder = models.Folder(name=folder.name, parent_id=folder.parent_id)
    db.add(db_folder)
    db.commit()
    return db_folder


def create_folder_by_path(db: Session, path: str) -> models.Folder:
    """
    Given a path-like string, recursively create folders.
    Args:
        db: SQLAlchemy Session
        path: path-like string

    Returns:
        The last folder specified in the path
    """
    p = path.split("/")
    curr = get_folder(db, 1)  # Root
    for f in p:

        match = list(
            db.execute(select(models.Folder).where(models.Folder.parent_id == curr.id and models.Folder.name == f)))
        if match:
            curr = match[0]
        else:
            curr = create_folder(db, schemas.FolderCreate(name=f, parent_folder_id=curr.id))
    return curr


def get_all_bookmarks(db: Session, skip: int = 0, limit: int = 100) -> Sequence[models.Bookmark]:
    return db.execute(select(models.Bookmark).offset(skip).limit(limit)).scalars().all()


def get_all_folders(db: Session) -> Sequence[models.Folder]:
    """
    Gets all the folders in the database
    """
    return db.execute(select(models.Folder)).scalars().all()


def get_all_bookmarks_in_folder(db: Session, folder_id: int) -> Sequence[models.Bookmark]:
    return db.get(models.Folder, folder_id).bookmarks


def get_parent_folder_of_bookmark(db: Session, bookmark_id: int) -> models.Folder:
    return db.get(models.Bookmark, bookmark_id).folder
