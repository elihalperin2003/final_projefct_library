from fastapi import APIRouter, HTTPException

from database.member_db import member_db

member_route = APIRouter()


@member_route.post("")
def create_member(name: str, email: str):
    data = {"name": name, "email": email, "active_is": True, "borrows_total": 0}
    member_db.create_member(data)


@member_route.get("")
def get_all_members():
    return member_db.get_all_members()


@member_route.get("/{id}")
def get_member_by_id(id: int):
    if not isinstance(id, int):
        raise HTTPException(422, f"{id} - is not a number")
    return member_db.get_member_by_id(id)


@member_route.patch("/{id}")
def update_member(id: int, name: str, email: str):
    if not isinstance(id, int):
        raise HTTPException(422, f"{id} - is not a number")
    data = {"name": name, "email": email}
    return member_db.update_member(id, data)


@member_route.patch("/{id}/deactivate")
def deactivate_member(id: int):
    if not isinstance(id, int):
        raise HTTPException(422, f"{id} - is not a number")
    member_db.deactivate_member(id)


@member_route.patch("/{id}/activate")
def activate_member(id: int):
    if not isinstance(id, int):
        raise HTTPException(422, f"{id} - is not a number")
    member_db.activate_member(id)
