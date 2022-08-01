from pathlib import Path

from bookie_backend.bookied.data.models import Base
from bookie_backend.bookied.deamon import app, get_db
from bookie_backend.bookied.utils import bookmark_parser
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

path = Path("test.sqlite")
if path.exists():
    path.unlink()
path.touch()

engine = create_engine(f"sqlite:///{path}", connect_args={"check_same_thread": False})

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_get_all_bookmarks_when_db_empty():
    response = client.get("/")
    data = response.json()
    assert data["bookmarks"] == [] and data["folders"] == []


def test_add_folder():
    response = client.post("/folder/", json={"path": "test"})
    data = response.json()
    assert (
        response.status_code == 201
        and data["path"] == "test"
        and isinstance(data["id"], int)
    )


def test_add_bookmark():
    bkmrk = {
        "url": "https://example.org",
        "path": "test",
        "name": "Example Domain",
        "description": "",
        "added": "1658014511",
    }
    response = client.post("/bookmark/", json=bkmrk)
    data = response.json()
    assert response.status_code == 201 and data == {
        "url": "https://example.org",
        "path": "test",
        "name": "Example Domain",
        "description": "",
        "added": 1658014511,
        "id": 1,
    }


def test_add_subfolder():
    response = client.post("/folder/", json={"path": "test/testing"})
    data = response.json()
    assert (
        response.status_code == 201
        and data["path"] == "test/testing"
        and isinstance(data["id"], int)
    )


def test_add_nested_bookmark():
    bkmrk = {
        "url": "https://example.com",
        "path": "test/testing",
        "name": "Example Domain",
        "description": "",
        "added": "1658014511",
    }
    response = client.post("/bookmark/", json=bkmrk)
    data = response.json()
    print(data)
    assert response.status_code == 201 and data == {
        "url": "https://example.com",
        "path": "test/testing",
        "name": "Example Domain",
        "description": "",
        "added": 1658014511,
        "id": 2,
    }


def test_try_add_existing_folder():
    response = client.post("/folder/", json={"path": "test"})
    data = response.json()
    assert response.status_code == 409 and data == {"detail": "Folder already exists"}


def test_try_add_existing_bookmark():
    bkmrk = {
        "url": "https://example.org",
        "path": "test",
        "name": "Example Domain",
        "description": "",
        "added": "1658014511",
    }
    response = client.post("/bookmark/", json=bkmrk)
    data = response.json()
    assert response.status_code == 409 and data == {"detail": "Bookmark already exists"}
