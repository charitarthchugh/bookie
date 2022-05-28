from pathlib import Path
from typing import Union

from bs4 import BeautifulSoup, PageElement, element


def get_parent_folder_tag(
    a_tag: Union[PageElement, element.Tag]
) -> Union[PageElement, element.Tag]:
    # Iterate to get to a dl
    # Previous sibling of a dl is an h3
    current_tag = a_tag
    while current_tag.name != "dl":
        current_tag = current_tag.parent
    outer = current_tag.previous_sibling
    outer_prev_sibling = [
        sibling for sibling in outer.previous_siblings if not sibling == "\n"
    ][0]
    return outer_prev_sibling


def get_path(h3_tag: Union[element.Tag, PageElement]) -> str:
    path_folder: list[str] = [h3_tag.string]

    parent_folder = h3_tag
    while parent_folder.name != "h1":
        parent_folder = get_parent_folder_tag(parent_folder)
        path_folder.append(parent_folder.string)
    return "/".join(reversed(path_folder))[1:]


def read(
    bookmarks: Path,
) -> dict[str, Union[list[str], list[dict[str, Union[str, int]]]]]:
    with open(bookmarks) as file:
        soup = BeautifulSoup(file, "html.parser")
    soup.h1.string = ""
    a_tags = soup.findAll("a")
    h3_tags = soup.findAll("h3")

    content = {"folders": [], "bookmarks": []}
    bkmrks = content["bookmarks"]
    for atag in a_tags:
        path = get_path(get_parent_folder_tag(atag))
        name = str(atag.string)
        name = " ".join(name.split())
        data = {
            "url": atag["href"],
            "added": int(atag["add_date"]),
            "name": name,
            "path": path,
        }
        if "TAGS" in atag.attrs.keys():
            data["tags"] = atag["tags"].split(",")
        bkmrks.append(data)
    folders = content["folders"]
    for h3tag in h3_tags:
        folders.append(get_path(h3tag))

    return content


if __name__ == "__main__":

    print(read(Path("./tests/test_bookmarks_file.html")))
