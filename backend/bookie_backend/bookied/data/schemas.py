from pydantic import BaseModel
from pydantic.networks import HttpUrl


class BookmarkBase(BaseModel):
    """Models a bookmark"""

    url: HttpUrl
    name: str
    description: str
    added: int
    path: str


class BookmarkCreate(BookmarkBase):
    #  folder: str
    pass


class Bookmark(BookmarkBase):
    id: int

    class Config:
        orm_mode = True


class FolderBase(BaseModel):
    path: str


# For consistancy
class FolderCreate(FolderBase):
    pass


class Folder(FolderBase):
    id: int
    children: list[Bookmark] = []

    class Config:
        orm_mode = True
