from dataclasses import dataclass
import json, uuid, datetime
from typing import List, Optional

@dataclass
class BookSeries:
    name: str
    total_parts: int


@dataclass
class Book:
    title: str
    author: str
    year: int
    genre: str
    read: bool = False
    series: Optional[BookSeries]
    id: str = uuid.uuid4()
    added_at: datetime = datetime.datetime.now()

    def masrk_as_read(self):
        self.read = True
    
    def __post_init__(self):
        if self.year > datetime.datetime.now().year:
            raise ValueError('Future date for year')
    
    def add_book(book: Book):
        pass

    def read_books():
        pass

    def unread_books():
        pass

    def find_by_author(author: str):
        pass

    def find_by_genre(genre: str):
        pass

    def find_by_series(series_name: str):
        pass

    def save_to_file(filepath: str):
        pass

    def load_from_file(filepath: str):
        pass
