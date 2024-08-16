from typing import Generator
from fastapi.testclient import TestClient

import pytest
from app.main import app


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c
