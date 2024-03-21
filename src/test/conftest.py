import pytest
import sys 
import os
from httpx import AsyncClient

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main import app

@pytest.fixture(scope="session")
def anyio_backend(): 
    return "asyncio"

@pytest.fixture(scope="session")
async def client(): 
    async with AsyncClient(app=app, base_url="http://test") as client:
        print("Client is ready")
        yield client