from typing import Optional

from pydantic import BaseModel
from pydantic.networks import HttpUrl


class BookmarkBase(BaseModel):
    """Models a bookmark"""

    url: HttpUrl
    name: str
    description: str
    added: int
    folder_id: int
    icon: Optional[str] = None


class BookmarkCreate(BookmarkBase):
    #  folder: str
    pass


class Bookmark(BookmarkBase):
    id: int

    class Config:
        orm_mode = True

    def __hash__(self):
        return hash(self.id)


class FolderBase(BaseModel):
    name: str
    parent_id: int
    bookmarks: Optional[list[Bookmark]] = []


# For consistency
class FolderCreate(FolderBase):
    pass


class Folder(FolderBase):
    id: int

    class Config:
        orm_mode = True
