from typing import Any, Union

from sqlalchemy.orm import Session

from . import models, schemas


def get_bookmark(db: Session, bookmark_id: int) -> models.Bookmark:
    return db.query(models.Bookmark).filter(models.Bookmark.id == bookmark_id).first()


def get_bookmark_by_url(db: Session, bookmark_url: str):
    return db.query(models.Bookmark).filter(models.Bookmark.url == bookmark_url).first()


def create_bookmark(db: Session, bookmark: schemas.BookmarkCreate) -> models.Bookmark:
    db_bookmark = models.Bookmark(
        name=bookmark.name,
        description=bookmark.description,
        added=bookmark.added,
        url=bookmark.url,
        parent_folder_id=bookmark.parent_folder_id,
        icon=bookmark.icon)
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)
    return db_bookmark


def get_folder(db: Session, folder_id: int) -> Union[models.Folder, Any]:
    return db.query(models.Folder).filter(models.Folder.id == folder_id).first()


# def get_folder_by_path(db: Session, folder_path: str) -> Union[models.Folder, Any]:
#     return db.query(models.Folder).filter(models.Folder.path == folder_path).first()
def get_folder_by_name(db: Session, name: str) -> Union[models.Folder, Any]:
    return db.query(models.Folder).filter(models.Folder.name == name)


def get_folders_by_parent_id(db: Session, parent_id: int) -> list[models.Folder]:
    # We are taking advantage of the fact that folders are created in order
    # So parent folders are always going to be created before the children
    return db.query(models.Folder).offset(parent_id).filter(models.Folder.parent_folder_id == parent_id)


def create_folder(db: Session, folder: schemas.FolderCreate) -> models.Folder:
    db_folder = models.Folder(name=folder.name, parent_folder_id=folder.parent_folder_id)
    db.add(db_folder)
    db.commit()
    db.refresh(db_folder)
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
    curr = get_folder(db, 0)  # Root
    for f in p:
        match = [x for x in get_folders_by_parent_id(db, parent_id=curr.id) if x.name == f]
        if match:
            curr = match[0]
        else:
            curr = create_folder(db, schemas.FolderCreate(name=f, parent_folder_id=curr.id))
    return curr


def get_all_bookmarks(db: Session, skip: int = 0, limit: int = 100) -> list[models.Bookmark]:
    return db.query(models.Bookmark).offset(skip).limit(limit).all()


def get_all_folders(db: Session) -> list[models.Folder]:
    """
    Gets all the folders in the database
    """
    return db.query(models.Folder).all()
