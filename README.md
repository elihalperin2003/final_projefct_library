תיאור המערכת:

המערכת מנהלת ספרייה באמצעות טבלת מנויים וטבלת ספרים.
פעולות המערכת:
1. צפייה בפרטי מנוי או פרטי ספר ספציפי, צפייה בכל הנתונים כולל סיכומים מיוחדים.
2. הוספת מנויים או ספרים חדשים.
3. שאילת ספרים והחזרתם.

פרטי ספר:
מספר זיהוי, כותר, מחבר, ז'אנר, זמינות, מספר זיהוי של שואל הספר (או ריק)

פרטי מנוי:
מספר זיהוי, שם, מייל, חבר פעיל, סך השאלות מצטבר.

---------------------------

creating docker with mysql

docker run --name mysql-w7
    -e MYSQL_ROOT_PASSWORD=root
    -e MYSQL_DATABASE=library_db
    -p 3306:3306
    -d mysql:8


---------------------------

```
final_project/
│
│
├── main.py
├── database/
│   ├── db_connection.py
│   ├── book_db.py
│   └── member_db.py
├── routes/
│   ├── book_routes.py
│   ├── member_routes.py
│   └── report_routes.py
├── logs/
│   └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore
```

---------------------------

מפרט ספר

id
מפתח ראשי

title
כותרת הספר, עמודה לא ריקה, מקסימום 50 תווים

author
שם המחבר, עמודה לא ריקה, מקסימום 50 תווים

genre
ערכים מותרים: ENUM
Fiction | Non-Fiction | Science | History | Other
כל ערך אחר מחזיר שגיאה
עמודה לא ריקה

is_available
האם הספר זמין להשאלה — FALSE מסמן הושאל
עמודה לא ריקה

borrowed_by_member_id
מזהה החבר ששואל את הספר
NULL אם זמין


מפרט מנוי

id
מפתח ראשי

name
שם החבר, עמודה לא ריקה, מקסימום 50 תווים

email
כתובת מייל — ייחודית, עמודה לא ריקה

is_active
האם החבר פעיל
FALSE לא יכול להשאיל
עמודה לא ריקה

total_borrows
מונה סה"כ השאלות — עולה ב-1 בכל השאלה
עמודה לא ריקה

---------------------------

system's roles

1
יצירת ספר
המשתמש שולח title/author/genre  
המערכת מוסיפה is_available=True, borrowed_by=NULL

2
genre
חייב להיות Fiction / Non-Fiction / Science / History / Other — כל ערך אחר מחזיר שגיאה
יש לוודא הן בהוספה (POST) והן בעדכון (PATCH)

3
יצירת חבר
המשתמש שולח name/email — המערכת מוסיפה is_active=True, total_borrows=0

4
email
חייב להיות ייחודי — אם קיים כבר מחזיר שגיאה

5
חבר לא פעיל
אם is_active=False — אי אפשר להשאיל ספר

6
ספר לא זמין
אי אפשר להשאיל ספר שכבר מושאל (is_available=False)

7
מקסימום ספרים
חבר לא יכול להחזיק יותר מ-3 ספרים בו-זמנית

8
החזרת ספר
ניתן להחזיר ספר רק אם הוא מושאל לאותו חבר שמחזיר אותו

---------------------------

endpoints

create_book(data)
POST /books

get_all_books()
GET /books

get_book_by_id(id)
GET /books/{id}

update_book(id, data)
PUT /books/{id}

set_available(id, val, member_id)
PUT /books/{id}/return/{member_id}

PUT /books/{id}/borrow/{member_id}

count_total_books()
GET /reports/summary

count_available_books()
GET /reports/summary

count_borrowed_books()
GET /reports/summary

count_by_genre(genre)
GET /reports/books-by-genre

count_active_borrows_by_member(member_id)
PUT /books/{id}/borrow/{member_id}

create_member(data)
POST /members

get_all_members()
GET /members

get_member_by_id(id)
GET /members/{id}

update_member(id, data)
PUT /members/{id}

deactivate_member(id)
PUT /members/{id}/deactivate

activate_member(id)
PUT /members/{id}/activate

increment_borrows(id)
PUT /books/{id}/borrow/{member_id}

count_active_members()
GET /reports/summary

get_top_member()
GET /reports/top-member

---------------------------

system's flow

creating in Docker before server's uploading
        ↓
connecting to container and creating database library_db
        ↓
uploading the server
        ↓
creating tables: book & member
        ↓
main menu: (options)

all options:
running the route
        ↓
validation the data typing (if exists)
        ↓
logic's system - 8 roles
        ↓
validation the data line according to table roles (if exists)
        ↓
running quary 

---------------------------

running

pip install -r requirements.txt
uvicorn main:app
