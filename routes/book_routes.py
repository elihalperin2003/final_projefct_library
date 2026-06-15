from fastapi import APIRouter, HTTPException

from database.book_db import book_db
from database.member_db import member_db

book_route = APIRouter()


@book_route.post("")
def create_book(title: str, author: str, genre: str):
    if genre not in ["Fiction", "Non-Fiction", "Science", "History", "Other"]:
        raise HTTPException(422, "is not correct genre")
    book_db.create_book({"title": title, "author": author, "genre": genre, "is_available": True})


@book_route.get("")
def get_all_books():
    return book_db.get_all_books()


@book_route.get("/{id}")
def get_book_by_id(id: int):
    if not isinstance(id, int):
        raise HTTPException(422, f"{id} - is not number")
    return book_db.get_book_by_id(id) or HTTPException(404, f"{id} - Not found")


@book_route.patch("/{id}")
def update_book(id: int, title: str, author: str, genre: str):
    if not isinstance(id, int):
        raise HTTPException(422, f"{id} - is not number")

    dct = {"title": title, "author": author, "genre": genre}
    return book_db.update_book(id, dct)


@book_route.patch("/{id}/borrow/{member_id}")
def borrow_book(id: int, member_id: int):
    if not isinstance(id, int) or not isinstance(member_id, int):
        raise HTTPException(422, f"{id} - is not number")
    book_db.set_availabla(id, False, member_id)
    member_db.increment_borrows(id)


@book_route.patch("/{id}/return/{member_id}")
def return_book(id: int, member_id: int):
    if not isinstance(id, int) or not isinstance(member_id, int):
        raise HTTPException(422, f"{id} - is not number")
    book_db.set_availabla(id, True, None)
