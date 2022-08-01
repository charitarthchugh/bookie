from typing import Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .data import crud, models, schemas
from .data.database import SessionLocal

app = FastAPI(title="Bookie Bookmark API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""Get Requests"""


@app.get("/", description="Get all folders and bookmarks")
async def get(db: Session = Depends(get_db)):
    return {
        "folders": crud.get_all_folders(db),
        "bookmarks": crud.get_all_bookmarks(db),
    }


@app.get(
    "/folders/",
    description="Get all folders (no search)",
    response_model=list[schemas.Folder],
)
async def get_folders(db: Session = Depends(get_db)):
    return crud.get_all_folders(db)


@app.get(
    "/bookmarks/",
    description="Get bookmarks, optionally with a query",
    response_model=list[schemas.Bookmark],
)
async def get_bookmarks(db: Session = Depends(get_db)):
    return db.query(models.Bookmark).all()


"""Post Requests"""


@app.post("/", status_code=404, response_description="Not allowed")
async def post():
    """There is nothing to return here, the request should be specific"""
    pass


@app.post(
    "/folder/",
    status_code=201,
    description="Add a folder at the specified path",
)
async def post_folder(folder: schemas.FolderCreate, db: Session = Depends(get_db)):
    db_folder = crud.get_folder_by_path(db, folder.path)
    if db_folder:
        raise HTTPException(409, detail="Folder already exists")
    return crud.create_folder(db, folder)


@app.post(
    "/bookmark/",
    status_code=201,
    response_model=schemas.Bookmark,
)
async def post_bookmark(
    bookmark: schemas.BookmarkCreate, db: Session = Depends(get_db)
):

    db_bookmark = crud.get_bookmark_by_url(db=db, bookmark_url=bookmark.url)
    if db_bookmark:
        raise HTTPException(409, detail="Bookmark already exists")
    if not crud.get_folder_by_path(db, bookmark.path):
        raise HTTPException(400, detail="Create Folder First")
    return crud.create_bookmark(db, bookmark)
