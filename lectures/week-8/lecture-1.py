# test_book_client.py
import pytest
from unittest.mock import patch, Mock
from requests.exceptions import Timeout
from book_client import BookClient

import requests

resp = requests.get("https://nul-pdi.netlify.app/api/books", timeout=10)
resp.raise_for_status()
for book in resp.json():
    print(f"{book["title"]} by {book["author"]}")

@pytest.fixture
def mock_success_response():
    response = Mock(status_code=200)
    response.json.return_value = [
        {"id": 4, "title": "The House in the Cerulean Sea", "author": "TJ Klune"}
    ]
    return response

@patch("book_client.requests.get")
def test_returns_books_on_success(mock_get, mock_success_response):
    mock_get.return_value = mock_success_response
    client = BookClient("https://nul-pdi.netlify.app")
    results: list[dict[str, object]] = client.list_books("Literary Fiction")
    
    return results.__len__()