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
Finally, run the server
```
python book_api/manage.py runserver
```
