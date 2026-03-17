# book_client.py
import requests
from requests.exceptions import Timeout, HTTPError

class BookClient:
    def __init__(self, base_url: str):
        self.base_url: str = base_url

    def list_books(self, genre: str | None = None) -> list[dict]:
        """Search the PDI book collection by genre."""
        try:
            response = requests.get(
                f"{self.base_url}/api/books",
                params={"genre": genre},
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except (Timeout, HTTPError):
            return []

    def create_book(self, title: str, author: str, year: int, genres: str, isbn: str, stock: int) -> dict:
        """Add a new book to the PDI collection."""
        try:
            response = requests.post(
                f"{self.base_url}/api/books",
                json={
                    "title": title,
                    "author": author,
                    "year": year,
                    "genres": genres,
                    "isbn": isbn,
                    "stock": stock
                },
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except (Timeout, HTTPError):
            return {}