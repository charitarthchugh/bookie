from pathlib import Path
from typing import Any, Union

from bookie_backend import  bookmark_parser





def test_parser_1():
    correct_result: dict[str, Union[list[str], list[dict[str, Union[str, int]]]]] = {
        "folders": ["Bookmarks bar", "Python", "Python/api", "Python/parse", "Flutter"],
        "bookmarks": [
            {
                "name": "PyPI · The Python Package Index",
                "url": "https://pypi.org/",
                "path": "Python",
                "added": 1652716428,
            },
            {
                "name": "Poetry - Python dependency management and packaging made easy",
                "url": "https://python-poetry.org/",
                "path": "Python",
                "added": 1652716495,
            },
            {
                "name": "Black documentation",
                "url": "https://black.readthedocs.io/en/stable/",
                "path": "Python",
                "added": 1652716351,
            },
            {
                "name": "Python Docs",
                "url": "https://docs.python.org/3/",
                "path": "Python",
                "added": 1652716283,
            },
            {
                "name": "FastAPI",
                "url": "https://fastapi.tiangolo.com/",
                "path": "Python/api",
                "added": 1652716876,
            },
            {
                "name": "lxml - Processing XML and HTML with Python",
                "url": "https://lxml.de/",
                "path": "Python/parse",
        
                "added": 1652716410,
            },
            {
                "name": "Flutter documentation | Flutter",
                "url": "https://docs.flutter.dev/",
                "path": "Flutter",
                "added": 1652716322,
            },
            {
                "name": "Nord",
                "url": "https://www.nordtheme.com/",
                "path": "Flutter",
                "added": 1652716786,
            },
            {
                "name": "Dart packages",
                "url": "https://pub.dev/",
                "path": "Flutter",
                "added": 1652716419,
            },
            {
                "name": "DuckDuckGo",
                "url": "https://duckduckgo.com/",
                "path": "",
                "added": 1652716374,
            },
        ],
    }

    bookmarks = bookmark_parser.read(Path("tests/test_bookmarks_file.html"))

    assert bookmarks == correct_result
