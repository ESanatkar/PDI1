# test_book_client.py
import pytest
from unittest.mock import patch, Mock
from book_client import BookClient


@pytest.fixture
def mock_list_response():
    response = Mock(status_code=200)
    response.json.return_value = [
        {"id": 1, "title": "Pachinko", "author": "Min Jin Lee"},
        {"id": 4, "title": "The House in the Cerulean Sea", "author": "TJ Klune"},
    ]
    return response


@patch("book_client.requests.get")
def test_list_books_returns_all_books(mock_get, mock_list_response):
    mock_get.return_value = mock_list_response
    client = BookClient("https://nul-pdi.netlify.app")
    results = client.list_books()

    assert len(results) == 2
    assert results[0]["title"] == "Pachinko"