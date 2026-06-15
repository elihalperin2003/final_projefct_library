from fastapi import FastAPI
from fastapi.responses import JSONResponse

from routes.book_routes import book_route
from routes.member_routes import member_route

# from database.db_connection import create_tables
from database.db_connection import db_connection as conn

from database.book_db import book_db
from database.member_db import member_db

app = FastAPI()

app.include_router(book_route, prefix="/books")
app.include_router(member_route, prefix="/members")


@app.exception_handler(Exception)
def except_handlers(req, e):
    return JSONResponse(500, "The server not working")
