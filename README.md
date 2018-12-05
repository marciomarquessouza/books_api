<img src="https://github.com/marciomarquessouza/books_api/blob/master/backend/book_api/books/static/books/images/logo_small_tales_black.png?v=3&s=200" title="FVCproductions" alt="FVCproductions">

# SMALL TALES API

> API using Python to create complete or partial PDFs from Database data.
> A simple Front-end using template was created to show the books, but a real front-end using VueJs is in development.

## Instructions

You will need virtualenv installed on your machine

```
sudo pip install virtualenv
```

You also need python3. Some distros already have it installed. Check if you have it

```
whereis python3
```

You will ned to create a virtual env. From here, all commands are running inside the folder "backend"

```
virtualenv venv
```

and activate it with the command below

```
source venv/bin/activate
```

So, run the requirements

```
pip install -r requirements.txt 
```

You can now start the the migrations, first makemigrations:

```
python book_api/manage.py makemigrations books
```

After that, run migrate:
```
python book_api/manage.py migrate
```

And load the database data with loaddata
```
python book_api/manage.py loaddata book_api/books.json 
```
Finally, run the server (with default port 8000)
```
python book_api/manage.py runserver
```

## PATHS:

front-end temporary): http://127.0.0.1:8000/

API

Books
(GET) List All Books: http://127.0.0.1:8000/book
(POST) Create a new book: http://127.0.0.1:8000/book
(GET) Book Detail: http://127.0.0.1:8000/${book_id}
(PUT) Update a book information: http://127.0.0.1:8000/book/${book_id}
(DELETE) delete a book: http://127.0.0.1:8000/book/${book_id}

Chapters
(GET) List All Chapters: http://127.0.0.1:8000/chapter
(POST) Create a new chapter: http://127.0.0.1:8000/chapter
(GET) Chapter Detail: http://127.0.0.1:8000/chapter/${book_id}
(PUT) Update a chapter information: http://127.0.0.1:8000/chapter/${chapter_id}
(DELETE) delete a chapter: http://127.0.0.1:8000/chapter/${chapter_id}
