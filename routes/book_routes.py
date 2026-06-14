from fastapi import APIRouter, HTTPException

from database.book_db import book_db

book_route = APIRouter()


@book_route.post("")
def create_book(title: str, author: str, genre: str):
    if genre not in ["Fiction", "Non-Fiction", "Science", "History", "Other"]:
        raise HTTPException(422, "is not correct genre")
    book_db.create_book({"title": title, "author": author, "genre": genre, "is_available": True})
